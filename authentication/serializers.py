from rest_framework import serializers
from .models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name','last_name','email','role']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','middle_name','last_name','email','role']