from django.conf.urls import url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import views
from . import models

app_name = 'characters'
slug_pattern = '[a-z\-_]+'

def detail_url(identifier, pattern):
    """
    Generates a url regex based on the passed identifier column name
    and the expected pattern.

    :param identifier: The model field used to select the record
        (e.g. 'pk' or 'slug')
    :type identifier: string
    :param pattern: Regular expression pattern for identifiers
    :type pattern: string or regexp
    :rtype: a detail url pattern
    """
    return r'^(?P<{}>{})/$'.format(identifier, pattern)

urlpatterns = [
    url(r'^$',
        ListView.as_view(model=models.Character),
        name='index'),
    url(detail_url('slug', slug_pattern),
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
        name='class_detail'),
    url(r'^races/$',
        ListView.as_view(model=models.Race),
        name='race_index'),
    url(r'^races/(?P<pk>[0-9]+)/$',
        DetailView.as_view(model=models.Race),
        name='race_detail')
]
