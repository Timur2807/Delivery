from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import OrderViewSet


router = DefaultRouter()
router.register(r'data', OrderViewSet)

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls)),
]
