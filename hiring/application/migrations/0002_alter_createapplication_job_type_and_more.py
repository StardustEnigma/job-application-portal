# Generated by Django 5.2.3 on 2025-06-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createapplication',
            name='job_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='createapplication',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
