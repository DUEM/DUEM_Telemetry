from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^motorjson', views.motorjson, name='motorjson'),
    url(r'^controlsjson', views.controlsjson, name='controlsjson'),
    url(r'^gpsjson', views.gpsjson, name='gpsjson'),
    url(r'^csvout', views.csvout, name='csvout'),
    url(r'^$',TemplateView.as_view(template_name='realtime/index.html'),name='index'),
]
