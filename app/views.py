import sys

from plain.auth.views import AuthViewMixin
from plain.passwords.views import PasswordLoginView, PasswordSignupView
from plain.runtime import __version__
from plain.views import TemplateView


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


class IndexView(BaseViewMixin, TemplateView):
    template_name = "index.html"
    html_title = "Home"
    login_required = False

    def get_template_context(self):
        context = super().get_template_context()
        context["message"] = "Welcome to Plain!"
        context["plain_version"] = __version__
        context["python_version"] = ".".join(map(str, sys.version_info[:3]))
        return context


class ExamplePrivateView(BaseViewMixin, TemplateView):
    template_name = "private.html"
    html_title = "Private"
    login_required = True


class LoginView(BaseViewMixin, PasswordLoginView):
    template_name = "login.html"
    login_required = False
    html_title = "Log in"


class SignupView(BaseViewMixin, PasswordSignupView):
    template_name = "signup.html"
    html_title = "Sign up"
    login_required = False
