from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Apps
from .serializers import (
    AppsSerializer, 
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AppsListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = AppsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        apps = Apps.objects.all()

        # if 'name' in self.request.query_params:
        #     name = self.request.query_params['name']
        #     apps = apps.filter(name__contains=name)

        return apps.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class AppsDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = AppsSerializer

    def get_queryset(self):
        return Apps.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)