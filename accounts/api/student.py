from accounts.models import Student, University
from accounts.utils.response import (
    CreatedResponse,
    FailureResponse,
    ResponseStatus,
    SuccessResponse,
)
from accounts.serializers import StudentSerializer, UniversitySerializer
from django.db import models
from django.db.models import Count, F, Q
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class StudentListCreateApiView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Student.objects.all()
    
    def get(self, request, *args, **kwargs):
        serializer = StudentSerializer(self.get_queryset(), many=True)
        return SuccessResponse(serializer.data)
    
    def post(self, request, *args, **kwargs):
        university = University.objects.filter(uid=self.kwargs.get("uid"))
        if university.exists():
            student = Student.objects.create(university=university, **request.data)
            serializer = StudentSerializer(student) 
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return CreatedResponse(serializer.data)
            return FailureResponse(serializer.errors)
        return FailureResponse({"message": ResponseStatus.MDNF.value})
    



class StudentRetreiveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Student.objects.all()
    
    def _get_object(self):
        return get_object_or_404(Student, uid=self.kwargs.get("uid"))
    
    def get(self, request, *args, **kwargs):
        student = self._get_object()
        serializer = StudentSerializer(student)
        return SuccessResponse(serializer.data)
    
    def put(self, request, *args, **kwargs):
        student = self._get_object()
        serializer = StudentSerializer(student)
        return SuccessResponse(serializer.data)

    def delete(self, request, *args, **kwargs):
        student = self._get_object()
        student.delete()        
        return SuccessResponse({"message": ResponseStatus.RDS.value})
    



class StudentAgeFilterRangeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        age_ranges = [
            (0, 18),
            (19, 25),
            (26, 35),
            (36, float('inf'))
        ]
        
        results = []
        for min_age, max_age in age_ranges:
            range_stats = Student.objects.filter(
                age__gte=min_age, 
                age__lte=max_age
            ).aggregate(
                males=Count('uid', filter=models.Q(gender='M')),
                females=Count('uid', filter=models.Q(gender='F'))
            )
            
            results.append({
                'age_range': f'{min_age}-{max_age}',
                'males': range_stats['males'],
                'females': range_stats['females']
            })
        
        return SuccessResponse(results)