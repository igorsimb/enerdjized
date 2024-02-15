from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_superuser']


admin.site.register(User, CustomUserAdmin)
