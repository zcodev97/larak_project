# Generated by Django 5.0.1 on 2024-02-25 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_user_id_userinfo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='locaiton',
            new_name='location',
        ),
    ]