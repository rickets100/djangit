"""djangit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hops/new/$', views.newhop, name='hopform'),
    url(r'^hops/(?P<id>[0-9]+)/edit/$', views.edithop, name='showhop'),
    url(r'^hops/(?P<id>[0-9]+)/$', views.onehop, name='showhop'),
    url(r'^hops/', views.hops, name='hops'),
    url(r'^admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^articles/2003/$', views.special_case_2003),
#     url(r'^articles/([0-9]{4})/$', views.year_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
# ]
