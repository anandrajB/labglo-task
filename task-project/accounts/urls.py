from django.urls import path
from accounts.api.student import (
    StudentListCreateApiView, 
    StudentRetreiveUpdateDestroyApiView,
    StudentAgeFilterRangeView
)
from accounts.api.university import (
    UniversityListCreateApiView, 
    UniversityRetreiveUpdateDestroyApiView
)
from .views import UserRegiratrationAPIView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("register/", UserRegiratrationAPIView.as_view(), name="user-registration"),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="token-obtrain-pair"),
    # Student URLs
    path('students/', StudentListCreateApiView.as_view(), name='student-list-create'),
    path('students/<uuid:uid>/', StudentRetreiveUpdateDestroyApiView.as_view(), name='student-detail'),
    path('students/range/', StudentAgeFilterRangeView.as_view(), name='student-age-range-stats'),
    # University URLs
    path('universities/', UniversityListCreateApiView.as_view(), name='university-list-create'),
    path('universities/<uuid:uid>/', UniversityRetreiveUpdateDestroyApiView.as_view(), name='university-detail'),
]
