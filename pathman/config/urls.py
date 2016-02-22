from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^classes/', include('classes.urls', namespace='classes')),
    url(r'^races/', include('races.urls', namespace='races')),
    url(r'^admin/', admin.site.urls)
]
