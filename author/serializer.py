from rest_framework import serializers
from .models import Author

class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')

class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
