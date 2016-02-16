from django.conf.urls import url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import views
from . import models

app_name = 'characters'
urlpatterns = [
    url(r'^$',
        ListView.as_view(model=models.Character),
        name='index'),
    url(r'^(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=models.Character),
        name='detail'),
    url(r'^new$',
        views.CharacterCreateView.as_view(),
        name='new'),
    url(r'^classes/$',
        ListView.as_view(model=models.CharacterClass),
        name='class_index'),
    url(r'^classes/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=models.CharacterClass),
        name='class_detail')
]
