# Generated by Django 4.2.7 on 2023-12-05 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0006_product_amount_delete_subcustomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='larak_app.product'),
        ),
    ]
