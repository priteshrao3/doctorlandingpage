# Generated by Django 4.2.4 on 2023-12-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_get_bonuses_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='get_bonuses',
            name='Main_Content',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='get_bonuses',
            name='Offer_Content',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='get_bonuses',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='get_bonuses',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
