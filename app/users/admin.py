from plain.admin.views import (
    AdminModelDetailView,
    AdminModelListView,
    AdminModelUpdateView,
    AdminViewset,
    register_viewset,
)
from plain.models.forms import ModelForm
from plain.urls import reverse

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["email"]


@register_viewset
class UserAdmin(AdminViewset):
    class ListView(AdminModelListView):
        model = User
        fields = [
            "id",
            "email",
            "created_at__date",
        ]
        queryset_order = ["-created_at"]
        search_fields = [
            "email",
        ]
        nav_icon = "people-fill"

        def get_object_links(self, obj):
            links = super().get_object_links(obj)
            links["Impersonate"] = reverse("admin:impersonate:start", obj.id)
            return links

    class DetailView(AdminModelDetailView):
        model = User

        def get_links(self):
            links = super().get_links()
            links["Impersonate"] = reverse("admin:impersonate:start", self.object.id)
            return links

    class UpdateView(AdminModelUpdateView):
        template_name = "admin/users/user_form.html"
        model = User
        form_class = UserForm

        def get_links(self):
            links = super().get_links()
            links["Impersonate"] = reverse("admin:impersonate:start", self.object.id)
            return links
