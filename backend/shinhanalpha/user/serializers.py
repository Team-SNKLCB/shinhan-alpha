from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, UserApps, UserReward, UserMission

class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Too short password')
        return make_password(value)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'ename', 'rrn', 'tel', 'status', 'tstamp')
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

class UserAppsSerializer(serializers.ModelSerializer):
    app_name = serializers.SerializerMethodField()
    app_description = serializers.SerializerMethodField()

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    def get_app_name(self, obj):
        return obj.app.name
    def get_app_description(self, obj):
        return obj.app.description
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required.')
        return value
    class Meta:
        model = UserApps
        fields = '__all__'

class UserRewardSerializer(serializers.ModelSerializer):
    reward_reward_name = serializers.SerializerMethodField()
    reward_tier_name = serializers.SerializerMethodField()
    reward_tier_point = serializers.SerializerMethodField()
    def get_reward_reward_name(self, obj):
        return obj.reward.reward_name
    def get_reward_tier_name(self, obj):
        return obj.reward.tier_name
    def get_reward_tier_point(self, obj):
        return obj.reward.tier_point
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required.')
        return value
    class Meta:
        model = UserReward
        fields = '__all__'

class UserMissionSerializer(serializers.ModelSerializer):
    # 미션 상태 변경 코드 필요
    mission_name = serializers.SerializerMethodField()
    mission_point  = serializers.SerializerMethodField()
    mission_description = serializers.SerializerMethodField()
    def get_mission_name(self, obj):
        return obj.mission.name
    def get_mission_point(self, obj):
        return obj.mission.point
    def get_mission_description(self, obj):
        return obj.mission.description

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required.')
        return value
    class Meta:
        model = UserMission
        fields = '__all__'

class UserPointSerializer(serializers.ModelSerializer):
    # mission_point  = serializers.SerializerMethodField()
    # mission_description = serializers.SerializerMethodField()
    # def get_mission_point(self, obj):
    #     return obj.mission.point
    # def get_mission_description(self, obj):
    #     return obj.mission.description

    # 포인트 합 구현 필요
    # total_point = serializers.SerializerMethodField()
    # def get_total_point(self, obj):
    #     return obj.mission_set.all().count()

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('user is required.')
        return value
    class Meta:
        model = UserMission
        fields = '__all__'