INSTALLED_PACKAGES = [
    "bolt.db",
    "bolt.tailwind",
    "bolt.auth",
    "bolt.passwords",
    "bolt.sessions",
    "bolt.admin",
    "bolt.htmx",
    "bolt.toolbar",
    "bolt.impersonate",
    "bolt.querystats",
    "users",
]

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    "bolt.middleware.security.SecurityMiddleware",
    "bolt.assets.whitenoise.middleware.WhiteNoiseMiddleware",
    "bolt.sessions.middleware.SessionMiddleware",
    "bolt.middleware.common.CommonMiddleware",
    "bolt.csrf.middleware.CsrfViewMiddleware",
    "bolt.auth.middleware.AuthenticationMiddleware",
    "bolt.middleware.clickjacking.XFrameOptionsMiddleware",
]
