# Generated by Django 4.1.5 on 2023-02-22 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpageapp', '0002_rename_cake_caken'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caken',
            new_name='Place',
        ),
    ]