from rest_framework import serializers
from orders.models import Orders


class OrdersSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Orders
        fields = '__all__'
