# Generated by Django 4.2.23 on 2025-07-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
