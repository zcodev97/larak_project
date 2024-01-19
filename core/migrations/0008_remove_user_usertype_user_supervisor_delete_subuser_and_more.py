# Generated by Django 5.0.1 on 2024-01-18 10:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userType',
        ),
        migrations.AddField(
            model_name='user',
            name='supervisor',
            field=models.ForeignKey(default='31dc0b00-85fd-49a1-9d4f-5a3345f5cb84', on_delete=django.db.models.deletion.PROTECT, related_name='user_supervisor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SubUser',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
