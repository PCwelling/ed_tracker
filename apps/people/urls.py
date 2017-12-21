from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.people_dashboard),
    url(r'^logout$', views.logout),
    url(r'^student_dashboard$', views.student_dashboard),
    url(r'^student_add$', views.student_add),
    url(r'^student_create$', views.student_create),
    url(r'^(?P<student_id>\d+)/student_view$', views.student_view),
]