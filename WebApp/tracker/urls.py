from django.conf.urls import url
from tracker import views

urlpatterns = [
    url(r'^activities/$', views.ActivityView.as_view()),
    url(r'^fields/$', views.FieldView.as_view()),
    url(r'^subfields/$', views.SubfieldView.as_view()),
]
