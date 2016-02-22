from django.conf.urls import url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import RedirectView

from util.urls import slug_url

from . import models

app_name = 'classes'

urlpatterns = [
    # 'classes/
    url(r'^$',
        ListView.as_view(model=models.Class),
        name='index'),

    # 'classes/slug_as_id/'
    url(slug_url(),
        RedirectView.as_view(pattern_name='detail'),
        name='detail-redirect'),
    # 'classes/slug_as_id.html'
    url(slug_url(extension='.html'),
        DetailView.as_view(model=models.Class),
        name='detail')
]
