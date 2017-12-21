from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.instructor_dashboard),
    url(r'^logout$', views.logout),
    url(r'^instructor_add$', views.instructor_add),
    url(r'^instructor_create$', views.instructor_create),
    url(r'^(?P<instructor_id>\d+)/instructor_view$', views.instructor_view),
]