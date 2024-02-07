# views.py
from datetime import datetime

import requests
from django.shortcuts import render, get_object_or_404
from .forms import MatchForm
from .models import Match


class MatchList:
    def __init__(self):
        self.api_url = "https://api.football-data.org/v4/matches"
        self.headers = {"X-Auth-Token": "e6952e6811684b4bb29ece2463aa5d16"}

    def get_live_matches(self):
        response = requests.get(self.api_url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('matches', [])
        return []

    @staticmethod
    def info_match(match):
        competition = match.get('competition', {}).get('name')
        team_home = match.get('homeTeam').get('name')
        teams_away = match.get('awayTeam').get('name')
        match_date = match.get('utcDate')
        if match_date:
            data = datetime.strptime(match_date, "%Y-%m-%dT%H:%M:%S%z")
        match_status = match.get('status')
        if match_status == "IN_PLAY" or match_status == "FINISHED":
            score_home = match.get('score', {}).get('fullTime', {}).get('home')
            score_away = match.get('score', {}).get('fullTime', {}).get('away')
            minutes = match.get('minute') if match_status == 'IN_PLAY' else ''
            score = f"{score_home} - {score_away}"
        else:
            score = ''
        live_match = match.get('liveStream', {}).get('url')
        return {
            'competition': competition,
            'team_home': team_home,
            'teams_away': teams_away,
            'minutes': minutes,
            'score': score,
            'match_datetime': data,
            'match_status': match_status,
            'live_match': live_match,
        }

    def list_matches(self):
        api_matches = self.get_live_matches()
        matches = [self.info_match(match) for match in api_matches]
        if not matches:
            matches.append({'message': 'Nu exista meciuri disponibile'})
        return matches


def match_list(request):
    match = MatchList()
    matches = match.list_matches()
    form = MatchForm()
    return render(request, 'list_of_matches.html', {'matches': matches, 'form': form})


class MatchLive:
    @staticmethod
    def match_live(request, match_id):
        match = get_object_or_404(Match, id=match_id)
        goals_home = match.goals_home.all()
        goals_away = match.goals_away.all()
        scorers_home = [goal.scorer for goal in goals_home]
        scorers_away = [goal.scorer for goal in goals_away]
        return render(request, 'live_match.html',
                      {'match': match, 'scorers_home': scorers_home, 'scorers_away': scorers_away})
