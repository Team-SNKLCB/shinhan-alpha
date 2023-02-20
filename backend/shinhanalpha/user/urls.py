from django.urls import path
from . import views

urlpatterns = [
    # path("/password", views.MemberChangePasswordView.as_view()),
    path("/signup", views.UserRegisterView.as_view()),
    path("/signin", views.UserLoginView.as_view()),
]