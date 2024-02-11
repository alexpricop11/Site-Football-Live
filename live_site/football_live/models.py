# models.py
from django.db import models


class Match(models.Model):
    league = models.CharField(max_length=200, default='')
    home_team = models.CharField(max_length=255, default='')
    away_team = models.CharField(max_length=255, default='')
    time = models.DateTimeField('utcDate')
    status = models.URLField(default='')
    objects = models.Manager()

    def __repr__(self):
        return f'{self.league}, {self.home_team},{self.away_team},{self.time}'

    def __str__(self):
        return f'{self.league}, {self.home_team},{self.away_team}'
