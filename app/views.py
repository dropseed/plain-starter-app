import sys
from typing import Any

from plain.auth.views import AuthView
from plain.passwords.views import PasswordLoginView, PasswordSignupView
from plain.runtime import __version__
from plain.views import TemplateView


# An example of a base view that can be used on almost all app views,
# to require login, set HTML title, and share other common functionality.
class BaseView(AuthView, TemplateView):
    html_title = ""

    def get_template_context(self) -> dict[str, Any]:
        context = super().get_template_context()
        context["html_title"] = self.get_html_title()
        return context

    def get_html_title(self) -> str:
        return self.html_title


class IndexView(BaseView):
    template_name = "index.html"
    html_title = "Home"
    login_required = False

    def get_template_context(self) -> dict[str, Any]:
        context = super().get_template_context()
        context["message"] = "Welcome to Plain!"
        context["plain_version"] = __version__
        context["python_version"] = ".".join(map(str, sys.version_info[:3]))
        return context


class ExamplePrivateView(BaseView):
    template_name = "private.html"
    html_title = "Private"
    login_required = True


class LoginView(BaseView, PasswordLoginView):
    template_name = "login.html"
    login_required = False
    html_title = "Log in"


class SignupView(BaseView, PasswordSignupView):
    template_name = "signup.html"
    html_title = "Sign up"
    login_required = False
