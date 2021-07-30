# Generated by Django 3.1.8 on 2021-06-02 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userportal', '0007_remove_userdata_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]