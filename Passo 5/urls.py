from django.conf.urls import include, urls
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
