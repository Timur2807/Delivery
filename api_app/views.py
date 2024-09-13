"""
В этом модуле лежит set представление.
"""

from rest_framework import viewsets
from orders.models import Orders
from .serializers import OrdersSerializers


class OrderViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для действий над заявками.

    Полный CRUD для сущностей заявок.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers

