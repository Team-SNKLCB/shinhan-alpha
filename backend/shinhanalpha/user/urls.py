from django.urls import path
from . import views

urlpatterns = [
    path("/signin", views.UserLoginView.as_view()),
    path("/apps", views.UserAppsView.as_view()),
    path("/reward", views.UserRewardView.as_view()),
    path("/mission", views.UserMissionView.as_view()),
    path("/point", views.UserPointView.as_view()),
    # path("/totalpoint", views.UserTotalPointView.as_view()),
    path("/<int:pk>", views.UserDetailView.as_view()),
    path("", views.UserListView.as_view()),
]