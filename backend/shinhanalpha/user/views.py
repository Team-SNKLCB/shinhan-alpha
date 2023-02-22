from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from .serializers import UserSerializer, UserAppsSerializer, UserRewardSerializer, UserMissionSerializer, UserPointSerializer, UserDetailSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from django.conf import settings
from .models import User, UserApps, UserReward, UserMission
from apps.models import Apps
from reward.models import Reward
from mission.models import Mission
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
import json

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
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):

    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        user = request.user
        serialized_user_data = self.serializer_class(user)
        response = Response({
                "user": serialized_user_data.data,
                }, status=status.HTTP_200_OK)
        return response

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        user = request.user

        if request.data.get('tier'):
            tier = request.data.get('tier')
            user.tier = tier

        if request.data.get('e_active'):
            e_active = request.data.get('e_active')
            user.e_active = e_active
        
        user.save()
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        e_active = user.e_active
        user.e_active = not e_active
        user.save()
        return Response(status=status.HTTP_200_OK)


class UserAppsView(
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAppsSerializer

    def get_queryset(self):
        userapps = UserApps.objects
        userapps = userapps.filter(user=self.request.user) \
            .select_related('app', 'user')
        return userapps.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        flag = request.data.get('flag')
        user_apps = UserApps.objects.get(id=id, user=self.request.user)

        user_apps.flag = flag
        user_apps.save()
        return Response(status=status.HTTP_200_OK)
    
class UserRewardView(
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserRewardSerializer

    def get_queryset(self):
        user_reward = UserReward.objects
        user_reward = user_reward.filter(user=self.request.user) \
            .select_related('reward', 'user')
        return user_reward.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        flag = request.data.get('flag')
        user_reward = UserReward.objects.get(id=id, user=self.request.user)

        user_reward.flag = flag
        user_reward.save()
        return Response(status=status.HTTP_200_OK)
    
class UserMissionView(
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserMissionSerializer

    def get_queryset(self):
        user_misson = UserMission.objects
        user_misson = user_misson.filter(user=self.request.user) \
            .select_related('mission', 'user')
        return user_misson.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        flag = request.data.get('flag')
        user_misson = UserMission.objects.get(id=id, user=self.request.user)

        user_misson.flag = flag
        user_misson.save()

        return Response(status=status.HTTP_200_OK)

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
        user_misson = user_misson.filter(user=self.request.user, flag=1) \
            .select_related('mission', 'user')
        return user_misson.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class UserTotalPointView(
    APIView,
):
    
    def get(self, request, *args, **kwargs):
        queryset = UserMission.objects.filter(user=request.user, flag=1)
        sum = queryset.aggregate(total_point=Sum('mission__point')).get('total_point')
        
        response = Response({
                "total_point": sum,
                }, status=status.HTTP_200_OK)
        return response