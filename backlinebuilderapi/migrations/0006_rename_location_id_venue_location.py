# Generated by Django 4.1 on 2022-09-01 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlinebuilderapi', '0005_rename_location_venue_location_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='location_id',
            new_name='location',
        ),
    ]
