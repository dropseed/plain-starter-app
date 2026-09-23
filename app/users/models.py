import hashlib
import zoneinfo
from datetime import datetime

from plain import postgres
from plain.passwords.types import PasswordField
from plain.postgres import Field, types
from plain.postgres.functions import Lower


@postgres.register_model
class User(postgres.Model):
    email: Field[str] = types.EmailField()
    password: Field[str] = PasswordField()
    is_admin: Field[bool] = types.BooleanField(default=False)
    created_at: Field[datetime] = types.DateTimeField(create_now=True)
    time_zone: Field[zoneinfo.ZoneInfo | None] = types.TimeZoneField(
        required=False, allow_null=True, default=None
    )

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
