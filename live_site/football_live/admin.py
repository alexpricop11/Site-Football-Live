from django.contrib import admin

from .models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('league', 'home_team', 'away_team', 'time', 'status')
