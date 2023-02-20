from .models import User
from django.contrib.auth.hashers import check_password
class UserAuth:

    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if not username or not password:
            if request.user.is_authenticated:
                return request.user
            return None
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if check_password(password, user.password):
            
            if user.status == '일반':
                print("A")
                return user

        return None

    def get_user(self, pk):
        try:
            member = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
        return member # if member.is_active and member.status == '일반' else None