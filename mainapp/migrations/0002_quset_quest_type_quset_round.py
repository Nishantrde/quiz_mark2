# Generated by Django 4.2.10 on 2024-07-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quset',
            name='quest_type',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='quset',
            name='round',
            field=models.CharField(default='', max_length=25),
        ),
    ]
