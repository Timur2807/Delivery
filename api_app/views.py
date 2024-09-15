"""
В этом модуле лежит set представление.
"""

from rest_framework import viewsets, generics
from orders.models import Orders
from .serializers import OrdersSerializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# class OrderAPIList(generics.ListCreateAPIView):
#     """
#     Набор представлений для действий над заявками.
#
#     Полный CRUD для сущностей заявок.
#     """
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers

class OrderAPIViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для действий над заявками.

    Полный CRUD для сущностей заявок.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_fields = ['id', 'city', 'package', 'customer']

    filterset_fields = [
        'id',
        'package',
        'status_order',
        'date_delivery',
        'city',
        'customer'
    ]
    ordering_fields = [
        'id',
        'city',
        'package',
        'customer'
    ]


