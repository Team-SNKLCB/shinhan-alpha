from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Too short password')
        return make_password(value)
    
    # def validate_email(self, value):
    #     if len(value.strip().rsplit('@', 1)) != 2:
    #         raise serializers.ValidationError('Not valid email')
    #     email_name, domain_part = value.strip().rsplit('@', 1)
    #     email = email_name + '@' + domain_part.lower()
    #     return email
    
    class Meta:
        model = User
        fields = ('id', 'pw', 'name', 'ename', 'rrn', 'tel', 'tier', 'is_active', 'status', 'tstamp')
        extra_kwargs = {
            "pw": {
                "write_only": True,
            },
        }