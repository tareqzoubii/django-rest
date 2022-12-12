from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ClubsSerializer
from .models import Clubs
# Create your views here.



class ClubsListView(ListCreateAPIView):
    queryset=Clubs.objects.all()
    serializer_class= ClubsSerializer


class ClubsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Clubs.objects.all()
    serializer_class= ClubsSerializer