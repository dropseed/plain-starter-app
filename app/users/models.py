from __future__ import annotations

import hashlib

from plain import postgres
from plain.passwords.types import PasswordField
from plain.postgres import types
from plain.postgres.functions import Lower


@postgres.register_model
class User(postgres.Model):
    email = types.EmailField()
    password = PasswordField()
    is_admin = types.BooleanField(default=False)
    created_at = types.DateTimeField(create_now=True)
    time_zone = types.TimeZoneField(required=False, allow_null=True)

    model_options = postgres.Options(
        constraints=[
            postgres.UniqueConstraint(
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
