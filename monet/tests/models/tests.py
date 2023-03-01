"""Tests Model"""

# Django
from django.db import models

# Models
from monet.utils.models import MonetModel
from monet.users.models.students import Student


class Test(MonetModel):
    """
    Test model for evaluate to students
    """

    name_test = models.CharField(
        verbose_name='Test Name',
        max_length=100,
        blank=False,
    )

    students = models.ManyToManyField(Student, through='TestStudent', related_name='tests')

    def __str__(self):
        return self.name_test


class TestStudent(MonetModel):
    test = models.ForeignKey(
        'Test',
        related_name='test_students',
        on_delete=models.SET_NULL,
        null=True
    )
    student = models.ForeignKey(
        Student,
        related_name='test_students',
        on_delete=models.SET_NULL,
        null=True
    )
    questions = models.ManyToManyField(
        'Question',
        through='TestStudentQuestionAnswer',
        related_name='test_student_answers'
    )

    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"""{self.test} - {self.student}"""


class TestStudentQuestionAnswer(MonetModel):
    test_student = models.ForeignKey(
        'TestStudent',
        related_name='tests_student_answers',
        on_delete=models.CASCADE,
    )

    question = models.ForeignKey(
        'Question',
        related_name='test_student_question',
        on_delete=models.CASCADE
    )

    student_answer = models.CharField(max_length=50, blank=True, null=True)
    question_points = models.PositiveSmallIntegerField(default=0)
    is_correct = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"""the answer is {self.is_correct}"""
