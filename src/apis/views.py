from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from pets.models import Pet
from apis.serializers import PetSerializer


# Create your views here.
class PetListCreateAPIView(ListCreateAPIView):
    model = Pet
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PetView(RetrieveUpdateDestroyAPIView):
    model = Pet
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
