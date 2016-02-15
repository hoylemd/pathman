from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^characters/', include('characters.urls'), namespace='characters'),
    url(r'^admin/', admin.site.urls, namespace='admin')
]
