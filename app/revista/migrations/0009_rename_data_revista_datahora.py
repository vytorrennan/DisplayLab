# Generated by Django 5.0 on 2024-01-11 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0008_alter_revista_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revista',
            old_name='data',
            new_name='dataHora',
        ),
    ]
