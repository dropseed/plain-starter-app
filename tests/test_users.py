from app.users.models import User


def test_user_avatar_url():
    user = User(email="test@example.com")
    assert (
        user.get_avatar_url()
        == "https://www.gravatar.com/avatar/55502f40dc8b7c769880b10874abc9d0?d=identicon"
    )
