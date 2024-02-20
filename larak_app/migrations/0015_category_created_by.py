# Generated by Django 5.0.1 on 2024-02-20 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0014_category_on_home_screen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(default='31dc0b00-85fd-49a1-9d4f-5a3345f5cb84', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]