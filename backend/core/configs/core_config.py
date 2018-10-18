# app/core/core_config.py
import os


# Application Settings
SITE_NAME = os.getenv("SITE_NAME", "DEFAULT")
BASE_DIR = os.path.abspath(
    os.path.dirname(os.getenv("FLASK_APP", "backend"))  # Find the root path

)
os.environ['BASE_DIR'] = BASE_DIR
SECRET_KEY = os.getenv("SECRET_KEY", "secret")  # Uses env variable in prod
CSRF_ENABLED = os.getenv("CSRF_ENABLED", True)
ROWS_PER_PAGE = 50

# Development Settings
PRODUCTION_MODE = os.getenv("FLASK_ENV", "development") == 'production'
DEBUG = not PRODUCTION_MODE  # Toggle off during release
DEBUG_TOOLBAR_ENABLED = not PRODUCTION_MODE  # Gives information about routes
NOISY_ERROR = PRODUCTION_MODE
USE_LOGGERS = os.getenv("USE_LOGGERS", False) or PRODUCTION_MODE
LOGS_DIR = os.getenv("LOGS_DIR", "instance/logs")

CORE_MODULE_ROUTES = {
    "Authorize": {
        "url": "/api/security/get-token",
        "methods": {}
    },
    "RefreshToken": {
        "url": "/api/security/refresh-token",
        "methods": {}
    }
}

