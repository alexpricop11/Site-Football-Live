# models.py
from django.db import models


class Match(models.Model):
    home_team = models.CharField(max_length=100, default='')
    away_team = models.CharField(max_length=100, default='')
    data = models.DateTimeField()
    score = models.CharField(max_length=70, default='')
    live_match = models.URLField(default='')
    objects = models.Manager()


    def __str__(self):
        return f'{self.home_team} {self.score} {self.away_team}'


class Team(models.Model):
    name = models.CharField(max_length=100, default='')
    logo_url = models.URLField(default='')
    objects = models.Manager()

    def __str__(self):
        return self.name
