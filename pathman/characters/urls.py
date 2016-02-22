from django.conf.urls import url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import RedirectView

from util.urls import slug_url

from . import views
from . import models

app_name = 'characters'

urlpatterns = [
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
