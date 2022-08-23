"""tanksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
# from main_app.views import MessagesAPIView, MessagesAPIList, MessagesAPIUpdate, MessagesAPIAllOperations
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from main_app.views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'messages', MessagesViewSet, basename='messages')

urlpatterns = [
                  path('', include('main_app.urls')),
                  path('chat/', include('chat_app.urls')),
                  path('admin/', admin.site.urls),
                  # path('api/v1/', include(router.urls)),
                  path('api/v1/messages_list', MessagesAPIList.as_view()),
                  path('api/v1/messages_list/<int:pk>', MessagesAPIUpdate.as_view()),
                  path('api/v1/messages_list_delete/<int:pk>', MessagesAPIDestroy.as_view()),

                  path('api/v1/auth_drf/', include('rest_framework.urls')),
                  path('api/v1/auth/', include('djoser.urls')),
                  re_path(r'^auth/', include('djoser.urls.authtoken')),

                  path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
