from plain.admin.views import (
    AdminModelDetailView,
    AdminModelListView,
    AdminModelUpdateView,
    AdminViewset,
    register_viewset,
)
from plain.models.forms import ModelForm

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

    class DetailView(AdminModelDetailView):
        model = User

    class UpdateView(AdminModelUpdateView):
        template_name = "admin/users/user_form.html"
        model = User
        form_class = UserForm
