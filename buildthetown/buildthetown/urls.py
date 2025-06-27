from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="django_admin"),
    path("blog/", include("blog_app.urls")),
    path("chat/", include("chat.urls")),
    path("obchod/", include("shop.urls")),
    path("sprava-webu/", include("website_management.urls")),
    path("", include("account.urls"), name="main_page"),
]
