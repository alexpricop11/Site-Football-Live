from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.match_list, name="FOOTBALL LIVE"),

]


urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
]
