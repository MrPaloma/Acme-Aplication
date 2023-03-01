# Generated by Django 3.2.5 on 2023-03-01 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time which the object was last modified', verbose_name='modified at')),
                ('question', models.CharField(max_length=200, verbose_name='Question')),
                ('points', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time which the object was last modified', verbose_name='modified at')),
                ('name_test', models.CharField(max_length=100, verbose_name='Test Name')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time which the object was last modified', verbose_name='modified at')),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time which the object was last modified', verbose_name='modified at')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tests.test')),
                ('answer', models.CharField(max_length=200, verbose_name='Answer for the question')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestStudentQuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time which the object was last modified', verbose_name='modified at')),
                ('student_answer', models.CharField(blank=True, max_length=50, null=True)),
                ('question_points', models.PositiveSmallIntegerField(default=0)),
                ('is_correct', models.BooleanField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_student_question', to='tests.question')),
                ('test_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_student_answers', to='tests.teststudent')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='teststudent',
            name='questions',
            field=models.ManyToManyField(related_name='test_student_answers', through='tests.TestStudentQuestionAnswer', to='tests.Question'),
        ),
        migrations.AddField(
            model_name='teststudent',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_students', to='users.student'),
        ),
        migrations.AddField(
            model_name='teststudent',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_students', to='tests.test'),
        ),
        migrations.AddField(
            model_name='test',
            name='students',
            field=models.ManyToManyField(related_name='tests', through='tests.TestStudent', to='users.Student'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test', to='tests.test'),
        ),
    ]
