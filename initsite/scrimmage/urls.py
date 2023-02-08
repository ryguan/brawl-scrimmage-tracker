from django.urls import path

from . import views


urlpatterns = [
    path('', views.search_bar, name='home'),
    path("external", views.index, name="index"),
    path("brawl-tag", views.search_bar, name="brawl-tag")
]