# Generated by Django 5.0 on 2024-01-11 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_itensdocarousel_carouselitem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='foto',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AddField(
            model_name='membro',
            name='saibaMais',
            field=models.CharField(default='', max_length=512),
        ),
    ]