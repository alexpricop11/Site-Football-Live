from django import forms
from .models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team_home', 'team_away', 'time', 'score',  'data', 'live_stream']
