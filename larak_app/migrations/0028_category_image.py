# Generated by Django 4.2.10 on 2024-03-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0027_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='test', upload_to='categories_images/'),
            preserve_default=False,
        ),
    ]