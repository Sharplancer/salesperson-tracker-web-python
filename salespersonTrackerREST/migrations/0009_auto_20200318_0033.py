# Generated by Django 2.2.10 on 2020-03-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salespersonTrackerREST', '0008_auto_20200318_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesperson',
            name='Photo',
            field=models.ImageField(upload_to='salesperson'),
        ),
    ]
