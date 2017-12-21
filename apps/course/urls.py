from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_dashboard),
    url(r'^logout$', views.logout),
    url(r'^course_type_add$', views.course_type_add),
    url(r'^course_type_create$', views.course_type_create),
    url(r'^(?P<course_type_id>\d+)/course_type_view$', views.course_type_view),
    url(r'^course_add$', views.course_add),
    url(r'^course_create$', views.course_create),
    url(r'^(?P<course_id>\d+)/course_view$', views.course_view),
    url(r'^remove_from_course$', views.remove_from_course),
    url(r'^add_to_course$', views.add_to_course),
]