from django.conf.urls import url, include

from charman import views

from rest_framework.routers import DefaultRouter

# API router
router = DefaultRouter()
router.register(r'characters', views.CharacterViewSet)

# finish up
urlpatterns = [
  url(r'^', include(router.urls)),
]
