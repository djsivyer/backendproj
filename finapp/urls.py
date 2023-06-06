from django.urls import path

from . import views

app_name = "finapp"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("homepage/", views.homepage, name="homepage"),
]