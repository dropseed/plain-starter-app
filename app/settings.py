INSTALLED_PACKAGES = [
    "plain.models",
    "plain.tailwind",
    "plain.auth",
    "plain.passwords",
    "plain.sessions",
    "plain.htmx",
    "plain.staff.admin",
    "plain.staff.toolbar",
    "plain.staff.impersonate",
    "plain.staff.querystats",
    # Local packages
    "users",
]

AUTH_USER_MODEL = "users.User"
AUTH_LOGIN_URL = "login"

MIDDLEWARE = [
    "plain.middleware.security.SecurityMiddleware",
    "plain.assets.whitenoise.middleware.WhiteNoiseMiddleware",
    "plain.sessions.middleware.SessionMiddleware",
    "plain.middleware.common.CommonMiddleware",
    "plain.csrf.middleware.CsrfViewMiddleware",
    "plain.auth.middleware.AuthenticationMiddleware",
    "plain.middleware.clickjacking.XFrameOptionsMiddleware",
    "plain.staff.querystats.QueryStatsMiddleware",
]

JINJA_LOADER = "plain.elements.ElementsLoader"
