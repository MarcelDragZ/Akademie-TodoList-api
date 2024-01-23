from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id'] 

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # creatorId = CurrentUserDefault()
    creatorId = serializers.PrimaryKeyRelatedField(read_only = True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'createdTime', 'creatorId', 'timePassed']