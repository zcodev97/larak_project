# Generated by Django 5.0.1 on 2024-02-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0013_alter_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='on_home_screen',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]