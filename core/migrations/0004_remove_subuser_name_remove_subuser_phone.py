# Generated by Django 4.2.7 on 2023-12-23 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subuser',
            name='phone',
        ),
    ]
