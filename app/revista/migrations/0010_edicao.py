# Generated by Django 5.0 on 2024-01-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0009_rename_data_revista_datahora'),
    ]

    operations = [
        migrations.CreateModel(
            name='edicao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('edicao', models.PositiveIntegerField(default=0, unique=True)),
            ],
        ),
    ]
