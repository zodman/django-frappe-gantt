# Generated by Django 2.0.3 on 2018-03-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_custom_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='custom_class',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]