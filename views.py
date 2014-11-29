from django.contrib.auth.models import User

from charman.models import Character, Alignment, Language, Size, Race, Skill, CharacterClass
from charman.serializers import CharacterSerializer, AlignmentSerializer, LanguageSerializer, SizeSerializer, RaceSerializer, SkillSerializer, CharacterClassSerializer
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

    # copy racial traits
    obj.size = obj.race.size
    obj.base_speed = obj.race.base_speed


class AlignmentViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = Alignment.objects.all()
  serializer_class = AlignmentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # IsAdminOrReadOnly

class LanguageViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = Language.objects.all()
  serializer_class = LanguageSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # IsAdminOrReadOnly

class SizeViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = Size.objects.all()
  serializer_class = SizeSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # IsAdminOrReadOnly

class RaceViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = Race.objects.all()
  serializer_class = RaceSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # IsAdminOrReadOnly

class SkillViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # IsAdminOrReadOnly

class CharacterClassViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides a 'list', 'create', 'retrieve',
  'update', and 'destroy' actions
  """
  queryset = CharacterClass.objects.all()
  serializer_class = CharacterClassSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # IsAdminOrReadOnly
