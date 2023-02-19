from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from ..shinhanalpha.settings import SIMPLE_JWT

# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = authenticate(id=request.data.get("id"), pw=request.data.get("pw"))
        if user is not None:
            serialized_user_data = self.serializer_class(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response({
                "user": serialized_user_data.data,
                "access_token": access_token
                }, status=status.HTTP_200_OK)
            response.set_cookie('refresh_token', refresh_token, expires=SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'], path=SIMPLE_JWT['AUTH_COOKIE_PATH'], httponly=SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'], secure=SIMPLE_JWT['AUTH_COOKIE_SECURE'])
            return response
        return Response({"error": "에러가 발생하였습니다."}, status=status.HTTP_400_BAD_REQUEST)