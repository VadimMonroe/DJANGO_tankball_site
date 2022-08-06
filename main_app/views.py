from re import A
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Messages
from .forms import MessagesForm
from django.views.generic import DetailView


def index(request):
    return render(request, 'main_app/index.html')


def about(request):
    return HttpResponse("<h4>About</h4>")


def tank_game(request):
    return render(request, 'main_app/tank_game.html')


def form_comments(request):
    error = ''
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form-comments')
        else:
            error = 'Форма была неверной'

    form = MessagesForm()
    all_messages_form = Messages.objects.all()

    data = {
        'form': form, 
        'all_messages_form': all_messages_form,
        'error': error
        }

    return render(request, 'main_app/form_comments.html', data)
