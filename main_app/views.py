import datetime
from re import A

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from .models import Messages, Category
from .forms import MessagesForm
from django.views.generic import DetailView, UpdateView, DeleteView

from rest_framework import generics, viewsets, mixins

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import MessagesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# class MessagesViewSet(mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       mixins.ListModelMixin,
#                       GenericViewSet):
#     # queryset = Messages.objects.all()
#     serializer_class = MessagesSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Messages.objects.all()[:3]
#
#         return Messages.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': [cats.form_name]})


class MessagesAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


class MessagesAPIList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = MessagesAPIListPagination


class MessagesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class MessagesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class MessagesAPIAllOperations(generics.RetrieveUpdateDestroyAPIView):
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
