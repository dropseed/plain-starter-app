URLS_ROUTER = "app.urls.AppRouter"

TIME_ZONE = "America/Chicago"

INSTALLED_PACKAGES = [
    "plain.postgres",
    "plain.tailwind",
    "plain.auth",
    "plain.passwords",
    "plain.sessions",
    "plain.htmx",
    "plain.toolbar",
    "plain.admin",
    "plain.elements",
    # Local packages
    "app.users",
]

AUTH_LOGIN_URL = "login"

MIDDLEWARE = [
    "plain.postgres.DatabaseConnectionMiddleware",
    "plain.sessions.middleware.SessionMiddleware",
    "app.middleware.TimezoneMiddleware",
    "plain.admin.AdminMiddleware",
]
