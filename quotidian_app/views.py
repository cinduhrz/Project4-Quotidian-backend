from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    # The Main Query for the index route
    # pass the model
    queryset = Todo.objects.all()
    # pass the serializer
    serializer_class = TodoSerializer
    # define permission class (optional)
    permission_classes = [permissions.AllowAny]