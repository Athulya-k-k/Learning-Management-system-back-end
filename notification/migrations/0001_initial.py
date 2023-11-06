# Generated by Django 4.1.5 on 2023-11-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_text', models.TextField()),
                ('notify_for', models.CharField(max_length=200)),
                ('notify_created_time', models.DateTimeField(auto_now_add=True)),
                ('notify_read_status', models.BooleanField(default=False)),
            ],
        ),
    ]