# Generated by Django 5.0.1 on 2024-02-23 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0024_order_invoice_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='invoice_id',
            new_name='order_id',
        ),
    ]
