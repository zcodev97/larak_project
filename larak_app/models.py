from django.db import models
import uuid
from django.conf import settings


class Categorie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='product_images/')  # Define ImageField
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    category = models.ForeignKey(Categorie,on_delete=models.PROTECT)
    amount = models.IntegerField()
    price = models.FloatField()
    cost = models.FloatField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField()
    status = models.JSONField()

    def __str__(self):
        return self.product.title


class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_id = models.CharField(max_length=10, unique=True, editable=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField()
    status = models.JSONField()
    def save(self, *args, **kwargs):
        if not self.invoice_id:
            # Generate a short and secure invoice ID
            self.invoice_id = self.generate_invoice_id()
        super().save(*args, **kwargs)

    def generate_invoice_id(self):
        # Customize the prefix or length as needed
        prefix = "INV"
        unique_id = str(uuid.uuid4().int)[:6]  # Extract 6 characters from the UUID
        return f"{prefix}-{unique_id}"


# {
#   "orderStatus": {
#     "clientOrderDate" :"2023-12-11 12:05 PM",
#     "orderAccepted" : {
#       "acceptedBy" : "Ahmed",
#       "dateAccpeted":"2023-12-11 12:05 PM"
#     },
#     "bikerPicked":{
#       "bikerName" : "Ali",
#       "date" : "2023-12-11 12:15 PM"
#     },
#     "orderDelieverd" : {
#         "date" :  "2023-12-11 12:45 PM"
#     }
#   }
# }