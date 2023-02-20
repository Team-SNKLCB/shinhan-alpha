from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Mission
from .serializers import (
    MissionSerializer, 
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MissionListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = MissionSerializer

    def get_queryset(self):
        return Mission.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MissionDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = MissionSerializer

    def get_queryset(self):
        mission = Mission.objects.all()
        return mission.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)