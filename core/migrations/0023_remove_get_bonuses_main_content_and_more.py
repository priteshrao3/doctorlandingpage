# Generated by Django 4.2.4 on 2023-12-25 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_get_bonuses_main_content_get_bonuses_offer_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='get_bonuses',
            name='Main_Content',
        ),
        migrations.RemoveField(
            model_name='get_bonuses',
            name='Offer_Content',
        ),
        migrations.RemoveField(
            model_name='get_bonuses',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='get_bonuses',
            name='modified_at',
        ),
    ]
