from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tank-game', views.tank_game, name='tank-game'),
    path('form-comments', views.form_comments, name='form-comments'),
    path('form-comments/<int:pk>', views.DetailMessageView.as_view(), name='message-detail'),
    path('form-comments/<int:pk>/update', views.DetailUpdateView.as_view(), name='message-update'),
    path('form-comments/<int:pk>/delete', views.DetailDeleteView.as_view(), name='message-delete'),
]
