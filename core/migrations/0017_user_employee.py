# Generated by Django 5.0.1 on 2024-02-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_rename_locaiton_userinfo_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee',
            field=models.JSONField(default={'': ''}),
            preserve_default=False,
        ),
    ]
