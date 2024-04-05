# Generated by Django 4.2.10 on 2024-04-01 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_user_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='supervisor',
            field=models.ForeignKey(default='4e7267d4-dc8a-4b6a-95ae-3e089d77bfe8', on_delete=django.db.models.deletion.PROTECT, related_name='user_supervisor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(default='65a75408-12f1-4cc7-b2a5-7f6a495a0aa0', on_delete=django.db.models.deletion.PROTECT, to='core.usertype'),
            preserve_default=False,
        ),
    ]
