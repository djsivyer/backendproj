from django.urls import path

from . import views

app_name = "finapp"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("logon", views.logon_view, name="logon"),
]