# Generated by Django 5.0 on 2024-01-12 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_membro_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membro',
            old_name='deletado',
            new_name='oculto',
        ),
    ]
