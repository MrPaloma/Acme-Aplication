"""Django models utilites."""

# Django
from django.db import models


class AcmeModel(models.Model):
    """
    This class is the basis for all templates
    attributes created and modified must be included in all template classes
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time which the object was created'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time which the object was last modified'
    )

    class Meta:
        """Meta customized"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
