# Generated by Django 5.0 on 2024-01-11 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0007_revista_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]