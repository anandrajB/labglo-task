from django.db.models import Count, Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import Student
from accounts.serializers import StudentSerializer
from accounts.utils.response import (
    CreatedResponse,
    FailureResponse,
    ResponseStatus,
    SuccessResponse,
)


class StudentListCreateApiView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return SuccessResponse(serializer.data)

    def create(self, request, *args, **kwargs):
        university_uid = request.data.get("university_uid")
        # university = get_object_or_404(University, uid=university_uid)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return CreatedResponse(serializer.data)


class StudentRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"

    def retrieve(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return SuccessResponse(serializer.data)

    def update(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessResponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        return SuccessResponse({"message": ResponseStatus.RDS.value})


class StudentAgeFilterRangeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        age_ranges = [(0, 18), (19, 25), (26, 35), (36, float("inf"))]
        # max_age calc base on gender
        results = []
        for min_age, max_age in age_ranges:
            filters = {"age__gte": min_age}
            if max_age != float("inf"):
                filters["age__lte"] = max_age

            range_stats = Student.objects.filter(**filters).aggregate(
                males=Count("uid", filter=Q(gender="Male")),
                females=Count("uid", filter=Q(gender="Female")),
            )
            results.append(
                {
                    "age_range": f"{min_age} - {int(max_age) if max_age != float('inf') else ' above_age'}",
                    "males": range_stats["males"],
                    "females": range_stats["females"],
                }
            )

        return SuccessResponse(results)
