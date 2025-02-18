import plain.admin.urls
import plain.assets.urls
from plain.auth.views import LogoutView
from plain.urls import RouterBase, include, path, register_router

from . import views


@register_router
class Router(RouterBase):
    urls = [
        include("assets/", plain.assets.urls),
        include("admin/", plain.admin.urls),
        path("logout/", LogoutView, name="logout"),
        path("login/", views.LoginView, name="login"),
        path("private/", views.ExamplePrivateView),
        path("signup/", views.SignupView, name="signup"),
        path("", views.HomeView),
    ]
