import hashlib

from plain import models
from plain.models.functions import Lower
from plain.passwords.models import PasswordField


class User(models.Model):
    email = models.EmailField()
    password = PasswordField()
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("email"),
                name="unique_lower_email",
            ),
        ]

    def __str__(self):
        return self.email

    def get_avatar_url(self):
        email_hash = hashlib.md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?d=identicon"
