import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'User Types'

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user_supervisor')
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    location = models.CharField(max_length=255,blank=True)
    lon = models.CharField(max_length=255,blank=True)
    lat = models.CharField(max_length=255,blank=True)

    class Meta:
        verbose_name_plural = 'Users'
