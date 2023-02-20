from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>", views.AppsDetailView.as_view()),
    path("", views.AppsListView.as_view()),
]