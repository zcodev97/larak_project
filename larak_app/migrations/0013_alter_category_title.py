# Generated by Django 5.0.1 on 2024-01-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0012_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]