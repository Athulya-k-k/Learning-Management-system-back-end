# Generated by Django 4.1.5 on 2023-11-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quizquestions_quiz_attemptquiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='attemptquiz',
            name='right_ans',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
