from bolt.urls import path
from bolt.views import TemplateView, View


class ExampleTemplateView(TemplateView):
    template_name = "example.html"

    def get_template_context(self):
        context = super().get_template_context()
        context["message"] = "Hello World!"
        return context


class ExampleJsonView(View):
    def get(self):
        return {"message": "Hello World!"}


class ExamplePlaintextView(View):
    def get(self):
        return "Hello World!"


urlpatterns = [
    path("json/", ExampleJsonView.as_view()),
    path("text/", ExamplePlaintextView.as_view()),
    path("", ExampleTemplateView.as_view()),
]
