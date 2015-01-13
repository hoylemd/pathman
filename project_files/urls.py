from django.conf.urls import patterns, include, url
from django.contrib import admin

from charman import views as charman_views
from simple_users import views as user_views

from rest_framework.routers import DefaultRouter

# API router
router = DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'sizes', charman_views.SizeViewSet)
router.register(r'races', charman_views.RaceViewSet)
router.register(r'skills', charman_views.SkillViewSet)
router.register(r'classes', charman_views.CharacterClassViewSet)
router.register(r'features', charman_views.FeatureViewSet)
router.register(r'feats', charman_views.FeatViewSet)
router.register(r'characters', charman_views.CharacterViewSet)
router.register(r'classlevels', charman_views.ClassLevelViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pathman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
      namespace='rest_framework')),
)
