from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Game, Player, Category, Review

class Games(ViewSet):
    def create(self, request):
        game = Game()
        game.title = request.data["title"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.year_released = request.data["yearReleased"]
        game.age_rec = request.data["ageRec"]
        game.play_time = request.data["playTime"]
        game.game_pic = request.data["gamePic"]
        game.rating = request.data["rating"]

        category = Category.objects.get(pk=request.data["categoryId"])
        game.category = category     
