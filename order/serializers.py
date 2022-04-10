from rest_framework import serializers
from .models import Order
from authentication.models import CustomUser
from book.models import Book
from datetime import timedelta, datetime

class BookHyperLinkedRelatedField(serializers.HyperlinkedRelatedField):

    def display_value(self, instance):
        return instance.name

class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = BookHyperLinkedRelatedField(view_name='book:rest_edit_book', queryset=Book.objects.all(),
                                       lookup_field='pk')

    class Meta:
        model = Order
        fields = ['user', 'book','plated_end_at', 'end_at']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at']

