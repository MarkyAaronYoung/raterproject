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

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)        
