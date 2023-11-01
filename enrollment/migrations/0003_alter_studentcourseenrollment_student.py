# Generated by Django 4.2.5 on 2023-10-31 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_delete_studentcourseenrollment'),
        ('enrollment', '0002_alter_studentcourseenrollment_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourseenrollment',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student', to='student.student'),
        ),
    ]