# Generated by Django 5.0 on 2024-01-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0012_rename_projetoimage_projetoimagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetoimagem',
            name='imagem',
            field=models.ImageField(upload_to='./projetos/uploads'),
        ),
    ]
