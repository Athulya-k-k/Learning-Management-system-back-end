# Generated by Django 4.2.5 on 2023-10-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='detail',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
