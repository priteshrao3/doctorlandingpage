# Generated by Django 4.2.4 on 2023-12-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_how_does_this'),
    ]

    operations = [
        migrations.AddField(
            model_name='who_attend',
            name='Content',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='who_attend',
            name='Title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='who_attend',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='who_attend',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]