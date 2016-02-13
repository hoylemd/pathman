from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.CharacterIndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.CharacterDetailView.as_view(),
        name='detail'),
    url(r'^new$', views.CharacterCreateView.as_view(), name='new')
]
