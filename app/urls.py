import plain.admin.urls
import plain.assets.urls
from plain.auth.views import LogoutView
from plain.urls import include, path

from . import views

urlpatterns = [
    path("assets/", include(plain.assets.urls)),
    path("admin/", include(plain.admin.urls)),
    path("logout/", LogoutView, name="logout"),
    path("login/", views.LoginView, name="login"),
    path("private/", views.ExamplePrivateView),
    path("signup/", views.SignupView, name="signup"),
    path("", views.HomeView),
]
