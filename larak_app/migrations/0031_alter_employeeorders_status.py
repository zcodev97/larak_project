# Generated by Django 4.2.10 on 2024-05-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0030_employeeorders_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeorders',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
