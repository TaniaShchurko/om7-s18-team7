from rest_framework import serializers
from .models import Book
from author.models import Author

class BookListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'author')

class BookDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(many=True, view_name='author-detail', read_only=True)
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'author')