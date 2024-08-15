import plain.assets.urls
import plain.staff.urls
import views
from plain.auth.views import LogoutView
from plain.urls import include, path

urlpatterns = [
    path("assets/", include(plain.assets.urls)),
    path("staff/", include(plain.staff.urls)),
    path("logout/", LogoutView, name="logout"),
    path("login/", views.LoginView, name="login"),
    path("public/", views.ExamplePublicView),
    path("signup/", views.SignupView, name="signup"),
    path("", views.HomeView),
]
