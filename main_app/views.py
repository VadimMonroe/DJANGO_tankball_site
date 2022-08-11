import datetime
from re import A

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Messages
from .forms import MessagesForm
from django.views.generic import DetailView, UpdateView, DeleteView

from rest_framework import generics
from .serializers import MessagesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class MessagesAPIView(APIView):
    def get(self, request):
        messages = Messages.objects.all()
        return Response({'messages': MessagesSerializer(messages, many=True).data})

    def post(self, request):
        serializer = MessagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None) # находим по первичному ключу

        # проверяем есть ли первичные ключи
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        # проверяем есть ли запись по этому ключу
        try:
            instance = Messages.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = MessagesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = Messages.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        instance.delete()

        return Response({"message": str(pk) + " deleted"})


# class MessagesAPIView(APIView):
#     def get(self, request):
#         messages_list = Messages.objects.all().values()
#         return Response({'messages': list(messages_list)})
#
#     def post(self, request):
#         post_new = Messages.objects.create(
#             form_name=request.data['form_name'],
#             message=request.data['message']
#         )
#         return Response({'post': model_to_dict(post_new)})


"""Общее значение для всего списка данных"""


# class MessagesAPIView(generics.ListAPIView):
#     queryset = Messages.objects.all()
#     serializer_class = MessagesSerializer


class DetailMessageView(DetailView):
    model = Messages
    template_name = 'main_app/detail_comment.html'
    context_object_name = 'message_detail'


class DetailUpdateView(UpdateView):
    model = Messages
    template_name = 'main_app/update_message.html'
    # fields = ['form_name', 'message']
    form_class = MessagesForm


class DetailDeleteView(DeleteView):
    model = Messages
    success_url = '/form-comments'
    template_name = 'main_app/delete_message.html'
    # fields = ['form_name', 'message']
    # form_class = MessagesForm


def index(request):
    return render(request, 'main_app/index.html')


async def about(request):
    now = datetime.datetime.now()
    html = f"<h4>{now}</h4>"
    return HttpResponse(html)


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
