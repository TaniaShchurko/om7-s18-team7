from rest_framework import serializers
from .models import Order
from authentication.models import CustomUser
from datetime import timedelta, datetime



class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ['user', 'book','plated_end_at', 'end_at']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at']

