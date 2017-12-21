from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.agency_dashboard),
    url(r'^logout$', views.logout),
    url(r'^agency_add$', views.agency_add),
    url(r'^agency_create$', views.agency_create),
    url(r'^(?P<agency_id>\d+)/agency_view$', views.agency_view),
]