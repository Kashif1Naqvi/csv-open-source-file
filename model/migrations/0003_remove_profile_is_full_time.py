# Generated by Django 3.1.4 on 2020-12-13 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20201213_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_full_time',
        ),
    ]