from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='home_page'),
    path("vsechny-prispevky/", views.all_post, name="all_post"),
    path('vsechny-prispevky/<slug:slug>', views.blog_detail,  name='blog_detail'),
    path("pravidla/", views.rules, name='rules'),
]