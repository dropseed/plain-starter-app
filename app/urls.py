from plain.admin.urls import AdminRouter
from plain.assets.urls import AssetsRouter
from plain.auth.views import LogoutView
from plain.urls import Router, include, path

from . import views


class AppRouter(Router):
    namespace = ""
    urls = [
        include("assets/", AssetsRouter),
        include("admin/", AdminRouter),
        path("logout/", LogoutView, name="logout"),
        path("login/", views.LoginView, name="login"),
        path("private/", views.ExamplePrivateView),
        path("signup/", views.SignupView, name="signup"),
        path("", views.IndexView, name="index"),
    ]
