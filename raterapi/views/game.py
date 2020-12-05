from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Game, Player, Category, Review

class Games(ViewSet):
    def list(self, request):
        games = Game.objects.all()

        serializer = GameSerializer(games, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        game = Game()
        game.title = request.data["title"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.year_released = request.data["yearReleased"]
        game.age_rec = request.data["ageRec"]
        game.play_time = request.data["playTime"]
        game.game_pic = request.data["gamePic"]
        game.rating = request.data["rating"]
        game.designer = request.data["designer"]

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

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'designer', 'description', 'year_released', 'number_of_players', 'play_time', 'age_rec', 'category', 'game_pic', 'rating')
        depth = 1
