from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from .serializers import UserSerializer, UserAppsSerializer, UserRewardSerializer, UserMissionSerializer, UserPointSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from django.conf import settings
from .models import User, UserApps, UserReward, UserMission
from apps.models import Apps
from reward.models import Reward
from mission.models import Mission
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserLoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            serialized_user_data = self.serializer_class(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response({
                "user": serialized_user_data.data,
                "access_token": access_token
                }, status=status.HTTP_200_OK)
            response.set_cookie('refresh_token', refresh_token, expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'], path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'], httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'], secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'])
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
        # is_active = 1
        res = self.create(request, args, kwargs)
        username = res.data.get('username')
        user = User.objects.get(username=username)

        for app in Apps.objects.all():
            UserApps(user=user, app=app).save()
        for reward in Reward.objects.all():
            UserReward(user=user, reward=reward).save()
        for mission in Mission.objects.all():
            UserMission(user=user, mission=mission).save()
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

class UserAppsView(
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAppsSerializer

    def get_queryset(self):
        userapps = UserApps.objects
        print(self.request.user)
        userapps = userapps.filter(user=self.request.user) \
            .select_related('app', 'user')
        return userapps.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    
class UserRewardView(
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserRewardSerializer

    def get_queryset(self):
        user_reward = UserReward.objects
        print(self.request.user)
        user_reward = user_reward.filter(user=self.request.user) \
            .select_related('reward', 'user')
        return user_reward.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    
class UserMissionView(
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserMissionSerializer

    def get_queryset(self):
        user_misson = UserMission.objects
        print(self.request.user)
        user_misson = user_misson.filter(user=self.request.user) \
            .select_related('mission', 'user')
        return user_misson.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    


class UserPointView(
    mixins.CreateModelMixin, 
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPointSerializer

    def get_queryset(self):
        user_misson = UserMission.objects
        print(self.request.user)
        user_misson = user_misson.filter(user=self.request.user) \
            .select_related('mission', 'user')
        return user_misson.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)