# Generated by Django 4.2.23 on 2025-07-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_campus_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(choices=[('LA', 'Los Angeles'), ('HTX', 'Houston'), ('NY', 'New York')], default='LA', max_length=3),
        ),
    ]
