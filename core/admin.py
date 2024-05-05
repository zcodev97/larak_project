from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserType
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

admin.site.unregister(Group)


class CustomGroupAdmin(GroupAdmin):
    list_display = ('id', 'name')  # Add 'id' to the list_display to show it in the admin


# Register the custom Group admin
admin.site.register(Group, CustomGroupAdmin)


@admin.register(User)
class SubCustomer(BaseUserAdmin):
    list_display = [
        "id",
        "username",
        'supervisor',
        'user_type',
        'first_name',
        'last_name',
        'location',
        'lon',
        'lat',
        'date_joined','is_active']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": (
            'supervisor',
            'user_type',
            'first_name',
            'last_name',
            'location',
            'lon',
            'lat',
        )}),
        (
            "Permissions",
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
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username", "password1", "password2",
                    'supervisor',
                    'user_type',
                    'first_name',
                    'last_name',
                    'location',
                    'lon',
                    'lat',
                ),
            },
        ),
    )
    list_per_page = 5  # Items per page
    ordering = ('-username',)  # Default ordering
    search_fields = ('username',)  # Fields to search by


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

# @admin.register(UserInfo)
# class UserInfoAdmin(admin.ModelAdmin):
#     list_per_page = 5  # Items per page
#     ordering = ('-user',)  # Default ordering
#     search_fields = ('user',)  # Fields to search by
#     list_display =  ['user', 'first_name', 'last_name', 'lon', 'lat']
#
