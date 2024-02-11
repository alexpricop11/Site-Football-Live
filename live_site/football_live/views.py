# views.py
import requests
from django.shortcuts import render


class MatchList:
    def __init__(self):
        self.api_url = "https://football-live-stream-api.p.rapidapi.com/index.php"
        self.headers = {
            "X-RapidAPI-Key": "6ac7c55484msh6892bddfe94b441p19d41cjsnaa77538b0915",
            "X-RapidAPI-Host": "football-live-stream-api.p.rapidapi.com"
        }

    def get_matches(self):
        response = requests.get(self.api_url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return data.get('matchId', [])
        return []

    @staticmethod
    def info_match(match):
        league = match.get('league')
        home_team = match.get('home_name')
        away_team = match.get('away_name')
        home_flag = match.get('home_flag')
        away_flag = match.get('away_flag')
        time = match.get('time')
        status = match.get('status')

        return {
            'league': league,
            'home_team': home_team,
            'away_team': away_team,
            'home_flag': home_flag,
            'away_flag': away_flag,
            'time': time,
            'status': status,
        }

    def list_matches(self):
        api_matches = self.get_matches()
        matches = [self.info_match(match) for match in api_matches]
        if not matches:
            matches.append({'message': 'Nu exista meciuri disponibile'})
        return matches


def match_list(request):
    match = MatchList()
    matches = match.list_matches()
    return render(request, 'home.html', {'matches': matches})
