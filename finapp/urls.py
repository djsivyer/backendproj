from django.urls import path

from . import views

app_name = "finapp"
urlpatterns = [
    path("/templates", views.index_view, name="index"),
]