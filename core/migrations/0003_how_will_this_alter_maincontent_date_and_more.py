# Generated by Django 4.2.4 on 2023-12-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_framework_steps_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='How_Will_This',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=200)),
                ('Content', models.TextField()),
                ('Image', models.ImageField(upload_to='How_Will_This_img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Dedicated',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Main_Title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Second_Content',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Third_Content',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Total_Hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Usefull',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='Why',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
