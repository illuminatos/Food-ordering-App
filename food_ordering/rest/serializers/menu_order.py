from rest_framework import serializers
from food_ordering.models.order import OrderModel


class MenuOrderSerialization(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"