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
    # 'classes/
    url(r'^classes/$',
        ListView.as_view(model=models.CharacterClass),
        name='class_index'),

    # 'races/slug_as_id/'
    url(slug_url(prefix='classes/'),
        RedirectView.as_view(pattern_name='characters:class-detail'),
        name='detail-redirect'),
    # 'classes/slug_as_id.html'
    url(slug_url(prefix='classes/', extension='.html'),
        DetailView.as_view(model=models.CharacterClass),
        name='class_detail'),

    # 'races/'
    url(r'^races/$',
        ListView.as_view(model=models.Race),
        name='race_index'),

    # 'races/slug_as_id/'
    url(slug_url(prefix='races/'),
        RedirectView.as_view(pattern_name='characters:race-detail'),
        name='detail-redirect'),
    # 'races/slug_as_id.html'
    url(slug_url(prefix='races/', extension='.html'),
        DetailView.as_view(model=models.Race),
        name='race_detail'),

    # root url
    url(r'^$',
        ListView.as_view(model=models.Character),
        name='index'),

    # 'new'
    url(r'^new$',
        views.CharacterCreateView.as_view(),
        name='new'),

    # 'slug_as_id/'
    url(slug_url(),
        RedirectView.as_view(pattern_name='characters:detail'),
        name='detail-redirect'),
    # 'slug_as_id.html'
    url(slug_url(extension='.html'),
        DetailView.as_view(model=models.Character),
        name='detail'),
    ]
