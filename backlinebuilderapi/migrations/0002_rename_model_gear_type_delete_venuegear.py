# Generated by Django 4.1 on 2022-09-01 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlinebuilderapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gear',
            old_name='model',
            new_name='type',
        ),
        migrations.DeleteModel(
            name='VenueGear',
        ),
    ]