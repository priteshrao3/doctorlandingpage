# Generated by Django 4.2.4 on 2023-12-25 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_faqs_created_at_faqs_modified_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqs',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='faqs',
            name='modified_at',
        ),
    ]