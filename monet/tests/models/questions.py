"""Question Model"""

# Django
from django.db import models

# Models
from monet.utils.models import MonetModel


class Question(MonetModel):
    """
    Question model for evaluate to students
    """
    test = models.ForeignKey(
        'Test',
        related_name='test',
        on_delete=models.SET_NULL,
        null=True
    )
    question = models.CharField(verbose_name='Question', max_length=200, blank=False)
    points = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.question
