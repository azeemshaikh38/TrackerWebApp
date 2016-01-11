from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^$', views.LoginAPIView.as_view()),
]
