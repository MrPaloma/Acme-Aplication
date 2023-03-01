""" Student model. """

# Django
from django.db import models

# Utilities
from monet.utils.models import MonetModel


class Student(MonetModel):
    """
        Student Model
        is a representation for all the students
    """
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to = 'users/pictures/',
        blank=True,
        null=True,
    )
    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """ Return user's string representation """
        return str(self.user)
