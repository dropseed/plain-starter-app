from plain.auth import get_request_user
from plain.http import HttpMiddleware
from plain.http.request import Request
from plain.http.response import Response
from plain.utils import timezone


class TimezoneMiddleware(HttpMiddleware):
    def before_request(self, request: Request) -> Response | None:
        user = get_request_user(request)
        if user and user.time_zone:
            timezone.activate(user.time_zone)
        else:
            timezone.deactivate()

        return None
