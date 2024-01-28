from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.core import serializers

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Todo.objects.all().order_by('-createdTime')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated # user must be logged in

    def create(self, request):
        todo = Todo.objects.create(title = request.POST.get('title', ''), description = request.POST.get('description', ''), creatorId = request.user)
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type = 'application/json')