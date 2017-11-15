from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^payload/', views.post, name = 'post'),
]
