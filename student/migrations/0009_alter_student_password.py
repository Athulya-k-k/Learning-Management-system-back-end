# Generated by Django 4.1.5 on 2023-11-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_student_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
