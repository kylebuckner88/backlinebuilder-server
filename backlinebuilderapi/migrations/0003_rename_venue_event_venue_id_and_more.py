# Generated by Django 4.1 on 2022-09-01 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlinebuilderapi', '0002_rename_model_gear_type_delete_venuegear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='venue',
            new_name='venue_id',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='location',
            new_name='location_id',
        ),
    ]