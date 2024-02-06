# views.py
from datetime import datetime, timezone
from urllib import request
import requests
from django.shortcuts import render, get_object_or_404
from .models import Match


def list_matches(request):
    api_url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": "e6952e6811684b4bb29ece2463aa5d16"}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        api_matches = response.json().get('matches', [])

        matches = []
        for match in api_matches:
            home_team = match.get('homeTeam', {}).get('name', '')
            away_team = match.get('awayTeam', {}).get('name', '')

            match_datetime_str = match.get('utcDate')
            live_match = match.get('liveStream', {}).get('url')

            if match.get('status') == "Live" or match.get('status') == "Finisat":
                score_home = match.get('score', {}).get('fullTime', {}).get('home', 0)
                score_away = match.get('score', {}).get('fullTime', {}).get('away', 0)
            else:
                score_home = score_away = ''

            if match_datetime_str:
                match_datetime = datetime.strptime(match_datetime_str, "%Y-%m-%dT%H:%M:%S%z")
                if match_datetime > datetime.now(timezone.utc):
                    match_status = 'Urmeaza'
                elif datetime.now(timezone.utc) >= match_datetime:
                    match_status = 'Live'
                else:
                    match_status = "Incheiat"
            else:
                match_status = "N/A"

            match_data = {
                'home_team': home_team,
                'away_team': away_team,
                'score': f"{score_home} - {score_away}",
                'match_datetime': match_datetime,
                'live_match': live_match,
                'match_status': match_status,
            }
            matches.append(match_data)
    if not matches:
        matches.append({'mesage': 'Nu exista meciuri disponibile'})

    return render(request, 'list_of_matches.html', {'matches': matches})


def match_live(requests, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'live_match.html', {'match': match})
