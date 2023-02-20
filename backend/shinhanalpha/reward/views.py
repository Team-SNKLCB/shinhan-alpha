from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Reward
from .serializers import (
    RewardSerializer, 
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RewardListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = RewardSerializer

    def get_queryset(self):
        return Reward.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class RewardDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = RewardSerializer

    def get_queryset(self):
        reward = Reward.objects.all()
        return reward.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)