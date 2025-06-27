from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="website_management_index"),
    path("souteze/", views.competition, name="website_management_competition"),
    path("kody/", views.codes, name="website_management_codes"),
    path("uzivatele/", views.users, name="website_management_users"),
]