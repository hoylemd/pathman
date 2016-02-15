from django.conf.urls import url

from . import views

app_name = 'characters'
urlpatterns = [
    url(r'^$', views.CharacterIndexView.as_view(),
        name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.CharacterDetailView.as_view(),
        name='detail'),
    url(r'^new$', views.CharacterCreateView.as_view(),
        name='new'),
    url(r'classes/$', views.CharacterClassIndexView.as_view(),
        name='class_index'),
    url(r'classes/(?P<pk>[0-9]+)/$', views.CharacterClassDetailView.as_view(),
        name='class_detail'),
    url(r'classes/new$', views.CharacterClassCreateView.as_view(),
        name='class_create')
]
