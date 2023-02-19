from .serializers import DictionarySerializer
from django.shortcuts import render
from .models import Dictionary
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DictionarySerializer
# Create your views here.


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [permissions.AllowAny]
