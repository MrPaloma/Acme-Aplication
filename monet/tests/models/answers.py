"""Answer Model"""

# Django
from django.db import models

# Models
from monet.utils.models import MonetModel
from monet.tests.models import Test


class Answer(MonetModel):
    """
    Answer model for evaluate to students
    """
    question = models.OneToOneField(
        Test,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    answer = models.CharField(verbose_name='Answer for the question', blank=False, max_length=200)

    def __str__(self):
        return f'''The answer is {self.answer}'''
