from django.contrib.auth.models import User

from charman.models import Character
from charman.serializers import CharacterSerializer
from charman.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import datetime

class CharacterViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = Character.objects.all()
  serializer_class = CharacterSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,
      IsOwnerOrReadOnly,)

  @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

  def pre_save(self, obj):
    obj.owner = self.request.user


