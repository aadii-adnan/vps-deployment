from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import categorySerializer


# Create your views here.
class categoryviewsets(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categorySerializer
