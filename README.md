# DisplayLab
Website oficial do laboratório Display do Instituto Federal do Norte de Minas Gerais

---

# Como rodar o projeto
### Variaveis de ambiente
- Crie um arquivo chamado .env dentro da pasta app e cole la o seguinte com os dados preenchidos:
```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

REDIS_PASSWORD=

SECRET_KEY=
DEBUG=
ADMIN_URL=
LOGIN_URL=

DROPBOX_ACCESS_TOKEN_FOR_BACKUP=
DROPBOX_REFRESH_TOKEN_FOR_BACKUP=
DROPBOX_APP_KEY=
DROPBOX_APP_SECRET=

DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_PASSWORD=
```

### Execute o projeto
- Em seguida tenha certeza de ter docker instalado, vá para a raiz do projeto e execute os seguintes comandos:

  `docker compose build`

  `docker compose up`
