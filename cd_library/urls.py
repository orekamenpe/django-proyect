from django.conf.urls import patterns, include, url
from cd_library import views

urlpatterns = patterns( '',
                        url(r'^search/$', views.search),
                        )