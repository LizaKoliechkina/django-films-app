from django.shortcuts import render
from django.http import HttpResponse

from .models import Actor
from .models import Film 
import string


def index(request):

    actor_names = [a.actor_name for a in Actor.objects.all()]
    return render(request, 'actors/index.html', {'actor_names': actor_names})


def index_hello(request):

    return HttpResponse('Hello, world! You are at the actors index.')


def films(request):

    films = Film.objects.all()
    return render(request, 'actors/films.html', {'films': films})


def details_actor(request, actor_name):

    actor =  Actor.objects.filter(actor_name=actor_name).first()
    film_list = actor.film_set.all()
    
    return render(request, 'actors/details_actor.html', {'films': film_list, 'actor': actor})


def details_film(request, film_name):          
        
    film = Film.objects.filter(film_name=film_name).first()

    actors = Actor.objects.all()
    result = [a.actor_name for a in actors if film.check_actor(a)] 

    return render(request, 'actors/details_film.html', {'film': film, 'actors': result})


def find(request):
    return render(request, 'actors/search_form.html', {})


def found_films(request):
    if request.method == 'POST':
        word = request.POST['search_term']
        films = Film.objects.all()
        result = [ f for f in films if f.search_film(word)]
    
    return render(request, 'actors/films.html', {'films':result})


def add_actor(request):
    return render(request, 'actors/add_actor.html', {})


def new_actor(request):
    if request.method == 'POST':
        new_name = request.POST['actor_name']
        new_country = request.POST['country']
        a = Actor.objects.create(actor_name=new_name, country=new_country)

    return render(request, 'actors/details_actor.html', {'actor': a})


def add_film(request):
    actors = Actor.objects.all()
    return render(request, 'actors/add_film.html', {'actors': actors})


def new_film(request):
    if request.method == 'POST':
        new_filmname = request.POST['film_name']
        new_filmyear = request.POST['film_year']
        f = Film.objects.create(film_name=new_filmname, film_year=new_filmyear)

        # actors_list = request.POST['actors']
        # f.actors.add(actors_list)

    return render(request, 'actors/details_film.html', {'film': f})






