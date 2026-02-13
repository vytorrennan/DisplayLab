<p>
  <img src="https://raw.githubusercontent.com/vytorrennan/DisplayLab/main/app/revista/static/imgs/paginaDePost/nascimentoVirtualDisplayLab/ifnmg.jpg" width="30%"/>
  <img src="https://raw.githubusercontent.com/vytorrennan/DisplayLab/main/app/revista/static/imgs/paginaDePost/nascimentoVirtualDisplayLab/logoNomeDiplay.png" width="27%"/>
</p>
<p>
  
</p>

# DisplayLab
Website oficial do laboratório Display do Instituto Federal do Norte de Minas Gerais

---

[Documentação do projeto pode ser encontrada aqui.](docs.md)

---

# Como rodar o projeto
### Variaveis de ambiente
- Crie um arquivo chamado .env dentro da pasta app e cole la o seguinte com os dados preenchidos:
```
```
POSTGRES_DB=displaylab
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password

REDIS_PASSWORD=your_redis_password

SECRET_KEY=your_django_secret_key
DEBUG=False
ADMIN_URL=/admin/
LOGIN_URL=/login/

DROPBOX_ACCESS_TOKEN_FOR_BACKUP=your_dropbox_access_token
DROPBOX_REFRESH_TOKEN_FOR_BACKUP=your_dropbox_refresh_token
DROPBOX_APP_KEY=your_dropbox_app_key
DROPBOX_APP_SECRET=your_dropbox_app_secret

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@displaylab.com
DJANGO_SUPERUSER_PASSWORD=your_secure_admin_password
```
```

### Execute o projeto
- Em seguida tenha certeza de ter docker instalado, vá para a raiz do projeto e execute os seguintes comandos:

  `docker compose build`

  `docker compose up`
