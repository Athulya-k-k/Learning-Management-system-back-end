# Generated by Django 4.1.5 on 2023-11-01 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_delete_studentcourseenrollment'),
        ('course', '0007_alter_course_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveBigIntegerField(default=0)),
                ('reviews', models.TextField(null=True)),
                ('course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_courses_rating', to='course.course')),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student_rating', to='student.student')),
            ],
        ),
    ]
