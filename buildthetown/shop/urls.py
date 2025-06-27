from django.urls import path
from . import views

urlpatterns = [
    path("budovi", views.shop_or_upgrades, {'page_type': 'shop'}, name='shop'),
    path("vylepseni", views.shop_or_upgrades, {'page_type': 'upgrade'}, name='upgrade'),
]
