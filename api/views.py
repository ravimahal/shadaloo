from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import generics
from .serializers import UnitSerializer
from units.models import Unit


# Create your views here.
class UnitView(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
