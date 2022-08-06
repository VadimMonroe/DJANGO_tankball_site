from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('tank-game', views.tank_game, name='tank-game'),
    path('form-comments', views.form_comments, name='form-comments'),
]
