# Generated by Django 5.0 on 2024-01-09 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0006_alter_projetos_pagina'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projetos',
            new_name='Projeto',
        ),
    ]