from plain.models.forms import ModelForm
from plain.staff.views import (
    StaffModelDetailView,
    StaffModelListView,
    StaffModelUpdateView,
    StaffModelViewset,
    register_viewset,
)

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["email"]


@register_viewset
class UserStaff(StaffModelViewset):
    class ListView(StaffModelListView):
        model = User
        fields = [
            "id",
            "email",
            "created_at__date",
        ]
        queryset_order = ["-created_at"]
        # get extra columns? custom, can't be ordered/filtered
        search_fields = [
            "email",
        ]

    class DetailView(StaffModelDetailView):
        model = User

    class UpdateView(StaffModelUpdateView):
        model = User
        form_class = UserForm
