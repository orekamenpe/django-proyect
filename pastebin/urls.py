from django.conf.urls import patterns, include, url
from pastebin import views

from models import Paste

urlpatterns = patterns('',
                       url(r'^$', views.PasteCreate.as_view(), name='paste_add'),
                       url(
                           r'^paste/(?P<slug>\d+)$',
                           views.PasteDetail.as_view(),
                           #{'queryset': Paste.objects.all()},
                           name='pastebin_paste_detail'),
                       url(r'^paste/$', views.PasteList.as_view(), {'queryset': Paste.objects.all()}, name='pastebin_paste_list'),
                       )
