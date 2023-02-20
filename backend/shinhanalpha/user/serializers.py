from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, UserApps, UserReward

class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Too short password')
        return make_password(value)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'ename', 'rrn', 'tel', 'tier', 'is_active', 'status', 'tstamp')
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