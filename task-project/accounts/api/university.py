from accounts.models import Student, University
from accounts.serializers import StudentSerializer, UniversitySerializer
from accounts.utils.response import (
    CreatedResponse,
    FailureResponse,
    ResponseStatus,
    SuccessResponse,
)
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UniversityListCreateApiView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return University.objects.all()
    
    def get(self, request, *args, **kwargs):
        serializer = UniversitySerializer(self.get_queryset(), many=True)
        return SuccessResponse(serializer.data)
    
    def post(self, request, *args, **kwargs):
        university = University.objects.create(**request.data)
        serializer = UniversitySerializer(university)
        return CreatedResponse(serializer.data)
    

class UniversityRetreiveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return University.objects.all()
    
    def _get_object(self):
        return get_object_or_404(University, uid=self.kwargs.get("uid"))
    def get(self, request, *args, **kwargs):
        university = self._get_object()
        serializer = UniversitySerializer(university)
        return SuccessResponse(serializer.data)
    
    def put(self, request, *args, **kwargs):
        university = self._get_object()
        serializer = UniversitySerializer(university)
        return SuccessResponse(serializer.data)

    def delete(self, request, *args, **kwargs):
        university =self._get_object()
        university.delete()
        return SuccessResponse({"message": ResponseStatus.RDS.value})
    