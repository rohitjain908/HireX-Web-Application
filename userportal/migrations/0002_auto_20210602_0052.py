# Generated by Django 3.1.8 on 2021-06-01 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userportal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='last_last',
            new_name='last_name',
        ),
    ]
