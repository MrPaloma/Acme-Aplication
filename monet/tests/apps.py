"""Tests app"""

# Django
from django.apps import AppConfig


class TestsAppConfig(AppConfig):
    """Tests app config"""
    name = 'monet.tests'
    verbose_name = 'Tests'
