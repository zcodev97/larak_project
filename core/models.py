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


    # {
    #     "user_type" : "user_type",
    #     "supervisor" : object,
    #     "user_info" : {
    #         "first_name" :  "first_name" ,
    #         "last_name": "last_name",
    #         "location": "location",
    #         "lon": "lon",
    #         "lat": "lat",
    #     }
    # }
    class Meta:
        verbose_name_plural = 'Users'
class UserInfo(models.Model):
    user = models.ForeignKey(User,  primary_key=True, on_delete=models.PROTECT, blank=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=False)
    lon = models.CharField(max_length=255, null=True)
    lat = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Users Info'

# class SubUser(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT , related_name="subuser")
#     supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name="supervisor")
#     created_at = models.DateTimeField(auto_now=True)
