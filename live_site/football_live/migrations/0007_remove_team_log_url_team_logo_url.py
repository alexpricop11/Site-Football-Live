# Generated by Django 5.0.1 on 2024-02-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_live', '0006_team_remove_match_log_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='log_url',
        ),
        migrations.AddField(
            model_name='team',
            name='logo_url',
            field=models.URLField(default=''),
        ),
    ]
