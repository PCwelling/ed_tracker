from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.store_dashboard),
    url(r'^logout$', views.logout),
    url(r'^store_add$', views.store_add),
    url(r'^store_create$', views.store_create),
    url(r'^(?P<store_id>\d+)/store_view$', views.store_view),
]