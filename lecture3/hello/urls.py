from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("mj", views.mj, name="mj"),
    path("kite", views.kite, name="kite")
]