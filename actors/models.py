from django.db import models

class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.actor_name


class Film(models.Model):
    film_name = models.CharField(max_length=400)
    film_year = models.IntegerField()
    #actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.film_name

    def search_film(self, word):
        return word in self.film_name

    def check_actor(self, Actor):
        return Actor in self.actors.all()
