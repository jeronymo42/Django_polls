# Generated by Django 4.2.6 on 2023-11-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_choice_votes_choice_голос'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='голос',
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='ов'),
        ),
    ]
