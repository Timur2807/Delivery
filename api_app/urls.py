from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *
#
#
router = DefaultRouter()
router.register(r'orders', OrderAPIViewSet)

app_name = 'orders'

urlpatterns = [
    path('api/', include(router.urls)),
]
