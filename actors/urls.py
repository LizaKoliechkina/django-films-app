from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.index_hello, name='index_hello' ),
    path('films', views.films, name='films'),
    path('<str:actor_name>/', views.details_actor, name='details_actor'),
    path('film/<str:film_name>/', views.details_film, name='details_film'),
    path('find', views.find, name='find'),
    path('found/films', views.found_films, name='found_films' ),
    path('add/actor', views.add_actor, name='add_actor'),
    path('newactor', views.new_actor, name='new_actor'),
    path('add/film', views.add_film, name='add_film'),
    path('newfilm', views.new_film, name='new_film'),
]