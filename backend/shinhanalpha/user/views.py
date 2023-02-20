from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from shinhanalpha.settings import SIMPLE_JWT
from .models import User, UserApps
from apps.models import Apps

# Create your views here.


class UserLoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = authenticate(id=request.data.get("id"), password=request.data.get("password"))
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
    

class UserListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.all()
        return user.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        res = self.create(request, args, kwargs)
        username = res.data.get('username')
        user = User.objects.get(username=username)
        for i in range(1, Apps.objects.count()+1):
            apps = Apps.objects.get(pk=i)
            UserApps(user=user,app=apps).save()
        return res
    
class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
