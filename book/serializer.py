from rest_framework import serializers
from .models import Book
from author.models import Author


class AuthorHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):

    def display_value(self, instance):
        return f'{instance.surname} {instance.name} {instance.patronymic}'


class BookListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'author')


class BookDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorHyperlinkedRelatedField(many=True, view_name='author:rest_edit_author', queryset=Author.objects.all(), lookup_field='pk')

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'author')