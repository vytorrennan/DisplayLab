#!/usr/bin/env bash

set -euo pipefail

scripts/wait-for-it.sh pgdb:5432 -t 30

case "${POSTGRES_DB}" in
    postgres|template0|template1)
        echo "Refusing to replace PostgreSQL maintenance database: ${POSTGRES_DB}" >&2
        exit 1
        ;;
esac

restore_token="$(date +%s)_$$"
restore_database="displaylab_restore_${restore_token}"
previous_database="displaylab_previous_${restore_token}"
media_restore_root="$(mktemp -d /tmp/displaylab-media-restore.XXXXXX)"
restore_database_exists=false
previous_database_exists=false

postgres_psql=(
    psql
    --host=pgdb
    --username="${POSTGRES_USER}"
    --dbname=postgres
    --set=ON_ERROR_STOP=1
)

drop_database() {
    local database_name="$1"

    PGPASSWORD="${POSTGRES_PASSWORD}" "${postgres_psql[@]}" \
        --set=database_name="${database_name}" <<'SQL'
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = :'database_name' AND pid <> pg_backend_pid();
DROP DATABASE IF EXISTS :"database_name";
SQL
}

cleanup() {
    local exit_status=$?

    if [[ "${restore_database_exists}" == true ]]; then
        drop_database "${restore_database}" >/dev/null 2>&1 || true
    fi

    rm -rf -- "${media_restore_root}"

    if [[ "${previous_database_exists}" == true ]]; then
        echo "The previous database was retained as ${previous_database}." >&2
    fi

    exit "${exit_status}"
}
trap cleanup EXIT

# Restore into a separate database first. Authentication, download, archive,
# and migration failures therefore leave the current database untouched.
PGPASSWORD="${POSTGRES_PASSWORD}" "${postgres_psql[@]}" \
    --set=restore_database="${restore_database}" <<'SQL'
CREATE DATABASE :"restore_database";
SQL
restore_database_exists=true

POSTGRES_DB="${restore_database}" python app/manage.py dbrestore --noinput
POSTGRES_DB="${restore_database}" python app/manage.py migrate --noinput --fake-initial
POSTGRES_DB="${restore_database}" python app/manage.py migrate --check
POSTGRES_DB="${restore_database}" python app/manage.py check

# The historical media archive contains application source too. Extract it in
# isolation now, then copy only the uploads after the database swap.
MEDIA_ROOT="${media_restore_root}" python app/manage.py mediarestore --noinput --replace

# Prevent new connections to the old database while the two names are swapped.
# Keep the previous database until the new one and its media pass final checks.
PGPASSWORD="${POSTGRES_PASSWORD}" "${postgres_psql[@]}" \
    --set=target_database="${POSTGRES_DB}" \
    --set=restore_database="${restore_database}" \
    --set=previous_database="${previous_database}" <<'SQL'
ALTER DATABASE :"target_database" WITH ALLOW_CONNECTIONS false;
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = :'target_database' AND pid <> pg_backend_pid();
ALTER DATABASE :"target_database" RENAME TO :"previous_database";
ALTER DATABASE :"restore_database" RENAME TO :"target_database";
SQL
restore_database_exists=false
previous_database_exists=true

python app/manage.py migrate --check
python app/manage.py check

replace_media_directory() {
    local relative_path="$1"
    local source_directory="${media_restore_root}/${relative_path}"
    local destination_directory="app/${relative_path}"
    local destination_parent
    local destination_name
    local replacement_directory
    local previous_directory

    [[ -d "${source_directory}" ]] || return 0

    destination_parent="$(dirname "${destination_directory}")"
    destination_name="$(basename "${destination_directory}")"
    mkdir -p "${destination_parent}"
    replacement_directory="$(mktemp -d "${destination_parent}/.${destination_name}.restore.XXXXXX")"
    previous_directory="${destination_parent}/.${destination_name}.previous.${restore_token}"
    cp -a "${source_directory}/." "${replacement_directory}/"

    if [[ -e "${destination_directory}" ]]; then
        mv "${destination_directory}" "${previous_directory}"
    fi

    if ! mv "${replacement_directory}" "${destination_directory}"; then
        if [[ -e "${previous_directory}" ]]; then
            mv "${previous_directory}" "${destination_directory}"
        fi
        return 1
    fi

    if [[ -e "${previous_directory}" ]]; then
        rm -rf -- "${previous_directory}"
    fi
}

for media_directory in \
    main/uploadsMain \
    projetos/uploadsProjetos \
    revista/uploadsRevista \
    alumni/uploadsAlunos
do
    replace_media_directory "${media_directory}"
done

if [[ -f "${media_restore_root}/alumni/default.jpg" ]]; then
    mkdir -p app/alumni
    default_image="$(mktemp app/alumni/.default.jpg.restore.XXXXXX)"
    cp -a "${media_restore_root}/alumni/default.jpg" "${default_image}"
    mv "${default_image}" app/alumni/default.jpg
fi

drop_database "${previous_database}"
previous_database_exists=false

echo "Database and media restore completed successfully."
