# Generated by Django 4.2.5 on 2023-11-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studentassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='student_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
