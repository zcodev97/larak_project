# Generated by Django 5.0.1 on 2024-02-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0019_delete_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]