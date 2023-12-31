# Generated by Django 4.2.4 on 2023-12-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_faqs_created_at_remove_faqs_modified_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='How_Does_This',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=200, null=True)),
                ('Content', models.CharField(blank=True, max_length=200, null=True)),
                ('Point_1', models.CharField(blank=True, max_length=200, null=True)),
                ('Point_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Point_3', models.CharField(blank=True, max_length=200, null=True)),
                ('Point_4', models.CharField(blank=True, max_length=200, null=True)),
                ('Content_in_Detail', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
