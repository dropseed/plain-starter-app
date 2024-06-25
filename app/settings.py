INSTALLED_PACKAGES = [
    "bolt.db",
    "bolt.tailwind",
    "bolt.auth",
    "bolt.passwords",
    "bolt.sessions",
    "bolt.htmx",
    "bolt.staff.admin",
    "bolt.staff.toolbar",
    "bolt.staff.impersonate",
    "bolt.staff.querystats",
    # Local packages
    "users",
]

AUTH_USER_MODEL = "users.User"
AUTH_LOGIN_URL = "login"

MIDDLEWARE = [
    "bolt.middleware.security.SecurityMiddleware",
    "bolt.assets.whitenoise.middleware.WhiteNoiseMiddleware",
    "bolt.sessions.middleware.SessionMiddleware",
    "bolt.middleware.common.CommonMiddleware",
    "bolt.csrf.middleware.CsrfViewMiddleware",
    "bolt.auth.middleware.AuthenticationMiddleware",
    "bolt.middleware.clickjacking.XFrameOptionsMiddleware",
    "bolt.staff.querystats.QueryStatsMiddleware",
]

JINJA_LOADER = "bolt.elements.ElementsLoader"
