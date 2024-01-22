from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = Todo.objects.all().order_by('-createdTime')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated # user must be logged in
