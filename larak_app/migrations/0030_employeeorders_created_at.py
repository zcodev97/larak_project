# Generated by Django 4.2.10 on 2024-05-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0029_employeeorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeorders',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
