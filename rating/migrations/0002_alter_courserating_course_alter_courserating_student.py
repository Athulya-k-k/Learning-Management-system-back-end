# Generated by Django 4.1.5 on 2023-11-02 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_delete_courserating'),
        ('student', '0004_delete_studentcourseenrollment'),
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserating',
            name='course',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
        migrations.AlterField(
            model_name='courserating',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
