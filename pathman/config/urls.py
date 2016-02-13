from django.conf.urls import include, url

urlpatterns = [
    url(r'^characters/', include('characters.urls'), name='index'),
]
