from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hops/new/$', views.newhop, name='hopform'),
    url(r'^hops/(?P<id>[0-9]+)/edit/$', views.edithop, name='edithop'),
    url(r'^hops/(?P<id>[0-9]+)/delete/$', views.deletehop, name='deletehop'),
    url(r'^hops/(?P<id>[0-9]+)/$', views.onehop, name='showhop'),
    url(r'^hops/', views.hops, name='hops'),
    url(r'^admin/', admin.site.urls),
]
