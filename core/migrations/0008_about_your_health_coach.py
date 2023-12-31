# Generated by Django 4.2.4 on 2023-12-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_who_attend_alter_awarded_by_awarded_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Your_Health_Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Health_Coach_img')),
                ('Title', models.CharField(blank=True, max_length=300, null=True)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Doctor_Speciality', models.CharField(blank=True, max_length=200, null=True)),
                ('Total_Franchise', models.CharField(blank=True, max_length=200, null=True)),
                ('Details_in_brif', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
