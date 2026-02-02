from __future__ import annotations

import hashlib
from datetime import datetime
from zoneinfo import ZoneInfo

from plain import models
from plain.models import types
from plain.models.functions import Lower
from plain.passwords.types import PasswordField


@models.register_model
class User(models.Model):
    email: str = types.EmailField()
    password: str = PasswordField()
    is_admin: bool = types.BooleanField(default=False)
    created_at: datetime = types.DateTimeField(auto_now_add=True)
    time_zone: ZoneInfo | None = types.TimeZoneField(required=False, allow_null=True)

    model_options = models.Options(
        constraints=[
            models.UniqueConstraint(
                Lower("email"),
                name="unique_lower_email",
            ),
        ],
    )

    def __str__(self) -> str:
        return self.email

    def get_avatar_url(self) -> str:
        email_hash = hashlib.md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?d=identicon"
