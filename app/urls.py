import bolt.staff.admin.urls
import views
from bolt.auth.views import LogoutView
from bolt.urls import include, path

urlpatterns = [
    path("favicon.ico", views.FaviconView),
    path("admin/", include(bolt.staff.admin.urls)),
    path("logout/", LogoutView, name="logout"),
    path("login/", views.LoginView, name="login"),
    path("public/", views.ExamplePublicView),
    path("signup/", views.SignupView, name="signup"),
    path("", views.HomeView),
]
