from django.urls import path

from . import views

app_name = "finapp"
urlpatterns = [
    path("", views.index),
]