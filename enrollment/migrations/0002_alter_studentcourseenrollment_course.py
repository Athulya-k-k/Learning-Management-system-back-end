# Generated by Django 4.2.5 on 2023-10-27 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourseenrollment',
            name='course',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_courses', to='course.course'),
        ),
    ]