from django.shortcuts import render
# 追加
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

# 追加
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()