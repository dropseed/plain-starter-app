from plain.test import Client


def test_homepage_exists():
    response = Client().get("/")
    assert response.status_code in (200, 301, 302)
