#!/usr/bin/env bash

set -euo pipefail

scripts/wait-for-it.sh pgdb:5432 -t 30

# A restore replaces this checkout's database. Resetting the schema first also
# removes objects and migration records left behind by a different branch.
PGPASSWORD="${POSTGRES_PASSWORD}" psql \
    --host=pgdb \
    --username="${POSTGRES_USER}" \
    --dbname="${POSTGRES_DB}" \
    --set=ON_ERROR_STOP=1 \
    --command='DROP SCHEMA public CASCADE; CREATE SCHEMA public;'

python app/manage.py dbrestore --noinput
python app/manage.py migrate --noinput --fake-initial

# Point MEDIA_ROOT to an isolated staging directory for this restore process.
# The historical media archive contains app source too, so copy only uploads.
media_restore_root=/tmp/displaylab-media-restore
MEDIA_ROOT="${media_restore_root}" python app/manage.py mediarestore --noinput --replace

for media_dir in \
    main/uploadsMain \
    projetos/uploadsProjetos \
    revista/uploadsRevista \
    alumni/uploadsAlunos
do
    source_dir="${media_restore_root}/${media_dir}"
    if [[ -d "${source_dir}" ]]; then
        mkdir -p "app/$(dirname "${media_dir}")"
        cp -a "${source_dir}" "app/$(dirname "${media_dir}")/"
    fi
done

if [[ -f "${media_restore_root}/alumni/default.jpg" ]]; then
    cp -a "${media_restore_root}/alumni/default.jpg" app/alumni/default.jpg
fi
