# Generated by Django 4.2.5 on 2023-09-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='full_name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='address',
            new_name='skills',
        ),
        migrations.AddField(
            model_name='teacher',
            name='mobile_no',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
