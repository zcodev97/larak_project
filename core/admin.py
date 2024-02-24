from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import  UserType,UserInfo


@admin.register(User)
class SubCustomer(BaseUserAdmin):
    list_display = ["id","username",'supervisor','user_type','date_joined']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ('supervisor','user_type')}),
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
                    "username", "password1", "password2", 'supervisor','user_type'),
            },
        ),
    )


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display =  ['user_id', 'first_name', 'last_name', 'lon', 'lat']



