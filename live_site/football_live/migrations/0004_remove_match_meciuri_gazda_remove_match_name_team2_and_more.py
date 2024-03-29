# Generated by Django 5.0.1 on 2024-02-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_live', '0003_rename_score_match_score_team1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='meciuri_gazda',
        ),
        migrations.RemoveField(
            model_name='match',
            name='name_team2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='score_team1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='score_team2',
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='live_match',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='match',
            name='score',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='match',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
