'''User models admin.'''

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from acme.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """User model admin."""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'created', 'modified')
