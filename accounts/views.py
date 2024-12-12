from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegistrationSerializer

from django.http import JsonResponse


def index(request):
    return JsonResponse({"message": "Hello World"})


class UserRegiratrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"access_token": str(AccessToken().for_user(user))})
