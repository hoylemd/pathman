from django.conf.urls import url

from .views import CharacterIndexView, CharacterDetailView, CharacterCreateView

app_name = 'characters'
urlpatterns = [
    url(r'^$', CharacterIndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', CharacterDetailView.as_view(), name='detail'),
    url(r'^new$', CharacterCreateView.as_view(), name='new')
]
