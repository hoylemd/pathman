from charman import models, serializers
from charman.permissions import IsOwnerOrReadOnly

from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route


class CharacterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def pre_save(self, obj):
        obj.owner = self.request.user

        # copy racial traits
        obj.size = obj.race.size
        obj.base_speed = obj.race.base_speed


class SizeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # IsAdminOrReadOnly


class RaceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.Race.objects.all()
    serializer_class = serializers.RaceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # IsAdminOrReadOnly


class SkillViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # IsAdminOrReadOnly


class CharacterClassViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.CharacterClass.objects.all()
    serializer_class = serializers.CharacterClassSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # IsAdminOrReadOnly


class FeatureViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.Feature.objects.all()
    serializer_class = serializers.FeatureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # IsAdminOrReadOnly


class FeatViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides a 'list', 'create', 'retrieve',
    'update', and 'destroy' actions
    """
    queryset = models.Feat.objects.all()
    serializer_class = serializers.FeatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # IsAdminOrReadOnly
