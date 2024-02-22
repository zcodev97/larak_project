from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    on_home_screen = models.BooleanField()
    created_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='product_images/')  # Define ImageField
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.IntegerField()
    price = models.FloatField()
    cost = models.FloatField()
    profit = models.FloatField(editable=False)  # Add a profit column
    discount = models.FloatField(editable=True)  # Add a discount column
    on_home_screen = models.BooleanField()
    on_banner = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Calculate and save the profit before saving the product instance
        self.profit = self.price - self.cost
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.JSONField()
    status = models.JSONField()
    created_at = models.DateTimeField(auto_now=True)


    # def save(self, *args, **kwargs):
    #     # Calculate and save the profit before saving the product instance
    #     self.price = self.product.price * self.amount
    #     super().save(*args, **kwargs)





# {
#     "1": {
#         "client_location": "location",
#         "description": "description"
#     },
#     "2": {
#         "user": 1,
#         "date": "currentDate"
#     },
#     "3": {
#         "biker": 12,
#         "date": "currentDate"
#     },
#     "order_delievered": {
#         "date": "currentDate"
#     }
# }
