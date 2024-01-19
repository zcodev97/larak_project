from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Invoice


@receiver(post_save, sender=Order)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        Invoice.objects.create(
            client=instance.client,
            product=instance.product,
            amount=instance.amount,
            price=instance.price,
            created_at=instance.created_at,
            status=instance.status
        )
