# Generated by Django 3.0.5 on 2020-04-04 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saladbowl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='stage',
            new_name='round',
        ),
    ]
