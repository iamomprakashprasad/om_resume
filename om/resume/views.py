from django.shortcuts import render
from rest_framework import generics
from .models import BasicInformation
from .serializers import BasicInformationSerializer
# Create your views here.

class BasicInformationList(generics.ListCreateAPIView):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer
