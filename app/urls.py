import bolt.admin.urls
import views
from bolt.auth.views import LogoutView
from bolt.urls import include, path

urlpatterns = [
    path("admin/", include(bolt.admin.urls)),
    path("logout/", LogoutView, name="logout"),
    path("login/", views.LoginView, name="login"),
    path("public/", views.ExamplePublicView),
    path("signup/", views.SignupView, name="signup"),
    path("", views.ExamplePrivateView),
]
