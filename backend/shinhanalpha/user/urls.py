from django.urls import path
from . import views

urlpatterns = [
    # path("/password", views.MemberChangePasswordView.as_view()),
    # path("/signup", views.UserRegisterView.as_view()),
    path("/signin", views.UserLoginView.as_view()),
    path("/apps", views.UserAppsView.as_view()),
    path("/<int:pk>", views.UserDetailView.as_view()),
    path("", views.UserListView.as_view()),

]