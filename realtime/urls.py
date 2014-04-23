from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^motorjson', views.motorjson, name='json'),
    url(r'^$',TemplateView.as_view(template_name='realtime/index.html'),name='index'),
]
