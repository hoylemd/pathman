from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/index.html')),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^classes/', include('classes.urls', namespace='classes')),
    url(r'^races/', include('races.urls', namespace='races')),
    url(r'^admin/', admin.site.urls)
]
