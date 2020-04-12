from django.db import models


class Word(models.Model):
    value = models.CharField(max_length=64)

    # Keep track of which round it is
    round = models.IntegerField(default=1)

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    creator = models.ForeignKey(
        "Player", on_delete=models.CASCADE, related_name="words"
    )

    def __str__(self):
        return self.value


class Player(models.Model):
    name = models.CharField(max_length=64)
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    score = models.IntegerField(default=0)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(unique=True, max_length=64)

    turn = models.IntegerField(default=0)  # zero-based turn numbers
    words_per_person = models.IntegerField(default=3)

    def __str__(self):
        return self.name
