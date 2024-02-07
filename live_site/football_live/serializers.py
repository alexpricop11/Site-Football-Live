from rest_framework import serializers
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'competition', 'teams', 'data', 'minute', 'score', 'live_match']
