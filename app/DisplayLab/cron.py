from django.core.management import call_command

def backup():
    try:
        print("Backup em andamento!")
        call_command('dbbackup')
        call_command('mediabackup')
        print("Backup feito!")
    except:
        print("Não foi possivel fazer o backup!")

def wrapper_coletar_noticias():
    try:
        print("Executando coleta de notícias via cron...")
        call_command('coletar_noticias')
        print("Coleta finalizada!")
    except Exception as e:
        print(f"Erro ao executar coleta de notícias: {e}")
