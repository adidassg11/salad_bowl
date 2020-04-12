from django.http import HttpResponse, Http404

# from django.template import loader
from django.shortcuts import get_object_or_404, render  # This replaces the two above ^^

from .models import Player, Word, Team, Game


def index(request):
    word_list = Word.objects.all()
    output = ", ".join([w.value for w in word_list])

    # template = loader.get_template("all_words.html")
    # context = {'latest_word_list': word_list}  # show "no available'.....
    context = {"all_words": word_list}

    # return HttpResponse("Hello, world. You're at the polls index. here are the words: {}".format(output))
    # return HttpResponse(template.render(context, request))
    return render(request, "all_words.html", context)


def word_detail(request, word_id):
    # try:
    #     word = Word.objects.get(id=word_id)
    # except Word.DoesNotExist:
    #     raise Http404

    ## ^^ all of this can be replaced with the following:
    word = get_object_or_404(Word, pk=word_id)
    game = word.game
    creator = word.creator

    print(game, game.name)
    return render(
        request, "word_detail.html", {"word": word, "game": game, "creator": creator}
    )


def word_results(request, word_id):
    response = "You're looking at the results of word %s."
    return HttpResponse(response % word_id)


def word_vote(request, word_id):
    return HttpResponse("You're voting on word %s." % word_id)


def word_create(request):
    return HttpResponse("You're going to create words here....")


def player_index(request):
    players = Player.objects.all()
    player_names = ", ".join([p.name for p in players])
    print(player_names)
    context = {"players": players}
    return render(request, "player.html", context)


def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    team = player.team  # Get other model
    words_created = player.words
    print(words_created)

    print(player.name, team.name)
    return render(
        request,
        "player_detail.html",
        {"player": player, "team": team, "words_created": words_created},
    )


def team_index(request):
    teams = Team.objects.all()
    context = {"teams": teams}
    return render(request, "teams.html", context)


def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    game = team.game  # Get other model

    return render(request, "team_detail.html", {"team": team, "game": game})


def game_index(request):
    games = Game.objects.all()
    context = {"games": games}
    return render(request, "games.html", context)


def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    return render(request, "game_detail.html", {"game": game})
