# Generated by Django 5.0 on 2024-01-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0010_rename_deletado_projeto_oculto'),
    ]

    operations = [
        migrations.CreateModel(
            name='projetoImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pasta', models.SlugField(default='', max_length=250)),
                ('imagem', models.ImageField(upload_to='')),
            ],
        ),
    ]
