from rest_framework import generics
from .models import Toy
from .serializers import ToySerializer
# from django.shortcuts import render


# Create your views here.
class ToyList(generics.ListCreateAPIView):
    # ListAPI View requires queryset and serializer
    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
