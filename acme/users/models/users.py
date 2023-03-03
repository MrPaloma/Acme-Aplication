"""User model"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from acme.utils.models import AcmeModel


class User(AcmeModel, AbstractUser):
    """ User model.

    Extends from django's Abstract User, change the username field to email
    and add some extra fields
    """
    email =  models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = 'Phone number must be between 1 and 15 characters long '
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self) -> str:
        """return username"""
        return self.username

    def get_short_name(self):
        """return the short name"""
        return self.username
