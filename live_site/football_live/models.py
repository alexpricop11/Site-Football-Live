# models.py
from django.db import models


class Match(models.Model):
    competition = models.CharField(max_length=200, default='')
    teams = models.CharField(max_length=255, default='')
    data = models.DateTimeField('utcDate')
    score = models.CharField(max_length=70, default='')
    minute = models.DateTimeField(auto_now=True)
    live_match = models.URLField(default='')
    objects = models.Manager()

    def __repr__(self):
        return f'{self.competition}, {self.teams},{self.score},{self.data},{self.minute}'

    def __str__(self):
        return f'{self.competition}, {self.teams}'


class Team(models.Model):
    name = models.CharField(max_length=100, default='')
    logo_url = models.URLField(default='')
    objects = models.Manager()

    def __str__(self):
        return self.name
