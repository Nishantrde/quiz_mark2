# Generated by Django 4.2.10 on 2024-07-21 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_team_list_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='qualified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
