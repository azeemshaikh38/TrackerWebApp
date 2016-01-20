from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^choose_fields/$', views.choose_fields, name="choose_fields"),
    url(r'^submit_fields/$', views.submit_fields, name="submit_fields"),
]
