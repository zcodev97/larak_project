import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, unique=True)
    is_supervisor = models.BooleanField(default=True)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                   related_name="supervisor_account")
