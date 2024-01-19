from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import  UserType


@admin.register(User)
class SubCustomer(BaseUserAdmin):
    list_display = ["id","username", "email", "first_name", "last_name", 'phone','supervisor','user_type','date_joined']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",'phone','supervisor','user_type')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username", "password1", "password2", 'phone', "email", "first_name", "last_name",'supervisor','user_type'),
            },
        ),
    )


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']



