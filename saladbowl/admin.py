from django.contrib import admin

from .models import Word, Player, Team, Game

admin.site.register(Word)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Game)
