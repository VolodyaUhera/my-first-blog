from . import views
from django.urls import include, path, re_path

urlpatterns = [
    path('', views.post_list, name='post_list'),
]