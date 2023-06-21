from django.urls import path,include

from . import views

app_name = "finapp"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("homepage/", views.home_view, name="homepage"),
    path("transactions/", views.transactions_view, name="transactions"),
    path("logout", views.logout_view, name="logout")
]