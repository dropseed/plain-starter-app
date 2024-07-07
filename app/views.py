import sys

from plain.auth.views import AuthViewMixin
from plain.http import FileResponse
from plain.passwords.views import PasswordLoginView, PasswordSignupView
from plain.runtime import APP_PATH
from plain.utils.version import get_version
from plain.views import TemplateView, View


# An example of a base mixin that can be used on almost all app views,
# to require login, set HTML title, and share other common functionality.
class BaseViewMixin(AuthViewMixin):
    html_title = ""

    def get_template_context(self):
        context = super().get_template_context()
        context["html_title"] = self.get_html_title()
        return context

    def get_html_title(self):
        """Override this method to set the HTML title dynamically."""
        return self.html_title


class FaviconView(View):
    def get(self):
        favicon_path = APP_PATH / "assets" / "favicon.ico"
        return FileResponse(favicon_path.open("rb"), content_type="image/x-icon")


class HomeView(BaseViewMixin, TemplateView):
    template_name = "home.html"
    html_title = "Home"

    def get_template_context(self):
        context = super().get_template_context()
        context["message"] = "Welcome to Plain!"
        context["plain_version"] = get_version()
        context["python_version"] = ".".join(map(str, sys.version_info[:3]))
        return context


class ExamplePublicView(HomeView):
    login_required = False
    html_title = "Public"


class LoginView(BaseViewMixin, PasswordLoginView):
    template_name = "login.html"
    login_required = False
    html_title = "Log in"


class SignupView(BaseViewMixin, PasswordSignupView):
    template_name = "signup.html"
    html_title = "Sign up"
    login_required = False
