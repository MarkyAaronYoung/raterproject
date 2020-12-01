from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    play_time = models.CharField(max_length=25)
    age_rec = models.CharField(max_length=25)
    category = models.ForeignKey("Category", on_delete=CASCADE)
    game_pic = models.ImageField()
    rating = models.IntegerField()
