# Generated by Django 4.2.7 on 2023-12-23 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.ForeignKey(default='86bac641-73f3-45a2-9a0f-b67b3f84ed31', on_delete=django.db.models.deletion.PROTECT, to='core.usertype'),
            preserve_default=False,
        ),
    ]