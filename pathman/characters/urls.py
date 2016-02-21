from django.conf.urls import url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import RedirectView

from . import views
from . import models

app_name = 'characters'


def detail_url(identifier, pattern, prefix='', extension=''):
    """
    Generates a url regex based on the passed identifier column name
    and the expected pattern.

    :param identifier: The model field used to select the record
        (e.g. 'pk' or 'slug')
    :type identifier: string

    :param pattern: Regular expression pattern for identifiers
    :type pattern: string or regexp

    :param prefix: Optional prefix on the url before the identifier
    :type prefix: string or regexp

    :rtype: a detail url pattern
    """
    suffix = extension if extension else '/?'
    return r'^{}(?P<{}>{}){}$'.format(prefix, identifier, pattern, suffix)


def slug_url(prefix='', extension=''):
    return detail_url('slug', '[a-z\-_]+',
                      prefix=prefix, extension=extension)


urlpatterns = [
    url(r'^$',  # root url
        ListView.as_view(model=models.Character),
        name='index'),
    url(r'^classes/$',  # 'classes/
        ListView.as_view(model=models.CharacterClass),
        name='class_index'),
    url(slug_url('classes/'),  # 'classes/slug_as_id'
        DetailView.as_view(model=models.CharacterClass),
        name='class_detail'),
    url(r'^races/$',  # 'races/slug_as_id'
        ListView.as_view(model=models.Race),
        name='race_index'),
    url(slug_url('races/'),  # 'races/slug_as_id'
        DetailView.as_view(model=models.Race),
        name='race_detail'),
    url(r'^new$',  # 'new'
        views.CharacterCreateView.as_view(),
        name='new'),
    url(slug_url(),
        RedirectView.as_view(pattern_name='characters:detail'),
        name='detail-redirect'),
    url(slug_url(extension='.html'),  # 'slug_as_id'
        DetailView.as_view(model=models.Character),
        name='detail'),
    ]
