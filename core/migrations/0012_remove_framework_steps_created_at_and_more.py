# Generated by Django 4.2.4 on 2023-12-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_framework_steps_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='framework_steps',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='framework_steps',
            name='modified_at',
        ),
    ]
