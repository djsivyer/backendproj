from django.urls import path, include

from . import views

app_name = "finapp"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
]