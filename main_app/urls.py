from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('tank-game', views.tank_game, name='tank-game'),
    path('form-comments', views.form_comments, name='form-comments'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
