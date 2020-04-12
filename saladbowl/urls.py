"""saladbowl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# TODO - at some point when separating these out into apps, see:
# https://docs.djangoproject.com/en/3.0/intro/tutorial03/#namespacing-url-names

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    # path('polls/', include('polls.urls')),  # Include other apps' urls
    # ex: /polls/
    path("", views.index, name="index"),  # FUTURE - change this to game landing page
    path("word/", views.index, name="index"),
    path("word/<int:word_id>/", views.word_detail, name="word_detail"),
    path("word/<int:word_id>/results/", views.word_results, name="results"),
    path("word/<int:word_id>/vote/", views.word_vote, name="vote"),
    path("word/create/", views.word_create, name="word_create"),
    path("player/", views.player_index, name="player_index"),
    path("player/<int:player_id>/", views.player_detail, name="player_detail"),
    path("team/", views.team_index, name="team_index"),
    path("team/<int:team_id>/", views.team_detail, name="team_detail"),
    path("game/", views.game_index, name="game_index"),
    path("game/<int:game_id>/", views.game_detail, name="game_detail"),
]
