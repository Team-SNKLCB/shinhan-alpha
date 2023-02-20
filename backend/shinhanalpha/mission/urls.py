from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>", views.MissionDetailView.as_view()),
    path("", views.MissionListView.as_view()),
]