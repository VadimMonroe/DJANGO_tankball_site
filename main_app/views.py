from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# получаем параметр request запрос
def index(request):
    return render(request, 'main_app/index.html')


def about(request):
    return HttpResponse("<h4>About</h4>")


def tank_game(request):
    return render(request, 'main_app/tank_game.html')


def form_comments(request):
    return render(request, 'main_app/form_comments.html')
