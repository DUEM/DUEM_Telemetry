from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^bmsjson', views.bmsjson, name='bmsjson'),
    url(r'^motorjson', views.motorjson, name='motorjson'),
    url(r'^controlsjson', views.controlsjson, name='controlsjson'),
    url(r'^gpsjson', views.gpsjson, name='gpsjson'),
    url(r'^mppt_woofjson', views.mppt_woofjson, name='mppt_woofjson'),
    url(r'^mppt_javedjson', views.mppt_javedjson, name='mppt_javedjson'),
    url(r'^csvout', views.csvout, name='csvout'),
    url(r'^$',TemplateView.as_view(template_name='realtime/index.html'),name='index'),
]
