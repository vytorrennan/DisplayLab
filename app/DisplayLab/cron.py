from django.core.management import call_command


def backup():
    try:
        print("Backup em andamento!")
        call_command('dbbackup')
        call_command('mediabackup')
        print("Backup feito!")
    except:
        print("Não foi possivel fazer o backup!")
