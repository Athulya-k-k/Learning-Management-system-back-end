# Generated by Django 4.1.5 on 2023-11-06 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_alter_teacher_password'),
        ('student', '0009_alter_student_password'),
        ('notification', '0004_notification_student_alter_notification_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notify_subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
