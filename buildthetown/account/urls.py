from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import MyLoginView

urlpatterns = [
    path("", views.index, name='home_page'),
    path("ucet/<slug:slug>", views.account_of_person, name='profile_page'),
    path("prihlaseni/", MyLoginView.as_view(template_name='account/login.html'), name="login"),
    path("odhlaseni/", auth_views.LogoutView.as_view(), name='logout'),
    path("registrace/", views.register, name="register"),
    path("zebricek/", views.ranking, name="ranking"),
    path("kody/", views.codes, name="codes"),
    path("aktuality", views.news, name='news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)