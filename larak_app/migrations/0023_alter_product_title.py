# Generated by Django 5.0.1 on 2024-02-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0022_rename_on_banner_home_screen_product_on_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]