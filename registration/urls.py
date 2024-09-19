from django.contrib.auth.views import LoginView
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *
#
#
router = DefaultRouter()
router.register(r'registration', RegistrationViewSet)


app_name = 'registration'

urlpatterns = [
    path('api/signup/', include(router.urls)),
]
