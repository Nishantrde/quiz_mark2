# Generated by Django 4.2.10 on 2024-07-22 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_team_qualified_alter_team_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='negative_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
