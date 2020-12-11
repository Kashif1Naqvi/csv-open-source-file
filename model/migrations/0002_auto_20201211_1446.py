# Generated by Django 3.1.4 on 2020-12-11 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.AddField(
            model_name='profile',
            name='JobTitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='AnnualSalary',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Department',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='AnualSalary',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='JobTitle',
        ),
    ]
