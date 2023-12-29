# Generated by Django 4.2.7 on 2023-12-24 08:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('larak_app', '0004_order_amount_order_client_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invocie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('invoice_id', models.CharField(editable=False, max_length=10, unique=True)),
            ],
        ),
    ]