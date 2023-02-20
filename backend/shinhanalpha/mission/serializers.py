from rest_framework import serializers
from .models import Mission

class MissionSerializer(serializers.ModelSerializer):
    # comment_count = serializers.SerializerMethodField()
    # like_count = serializers.SerializerMethodField()
    
    # def get_comment_count(self, obj):
    #     return obj.comment_set.all().count()

    # def get_like_count(self, obj):
    #     return obj.like_set.all().count()

    class Meta:
        model = Mission
        fields = '__all__'