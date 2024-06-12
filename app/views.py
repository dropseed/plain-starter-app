import sys

from bolt.auth.views import AuthViewMixin
from bolt.passwords.views import PasswordLoginView, PasswordSignupView
from bolt.utils.version import get_version
from bolt.views import TemplateView


class BaseViewMixin(AuthViewMixin):
    html_title = ""

    def get_template_context(self):
        context = super().get_template_context()
        context["html_title"] = self.get_html_title()
        return context

    def get_html_title(self):
        """Override this method to set the HTML title dynamically."""
        return self.html_title


class ExamplePrivateView(BaseViewMixin, TemplateView):
    template_name = "home.html"

    def get_template_context(self):
        context = super().get_template_context()
        context["message"] = "Welcome to Bolt!"
        context["bolt_version"] = get_version()
        context["python_version"] = ".".join(map(str, sys.version_info[:3]))
        return context


class ExamplePublicView(ExamplePrivateView):
    login_required = False


class LoginView(BaseViewMixin, PasswordLoginView):
    login_required = False
    html_title = "Login"


class SignupView(BaseViewMixin, PasswordSignupView):
    template_name = "signup.html"
    html_title = "Sign Up"
    login_required = False
