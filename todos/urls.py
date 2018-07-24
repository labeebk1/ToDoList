from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name="add"),
    url(r'^details/(?P<id>\w{0,500})/$', views.details),
    url(r'^delete/(?P<id>\w{0,500})/$', views.delete),
    url(r'^modify/(?P<id>\w{0,500})/$', views.modify, name='modify'),
]