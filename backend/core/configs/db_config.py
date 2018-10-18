import os

BASE_DIR = os.getenv(
    "BASE_DIR",
    os.path.abspath(os.path.dirname(os.getenv("FLASK_APP", "backend")))
)

# SQLAlchemy Settings
DB_TYPE = os.getenv("DB_TYPE", "")
USER = os.getenv('DB_USER', '')
PWD = os.getenv('DB_PW', '')
DB_HOST = os.getenv('HOST', '')
DB_NAME = os.getenv('DB_NAME', '')
SQLALCHEMY_DATABASE_URI = '{type}://{user}:{pwd}@{host}/{name}'.format(
    type=DB_TYPE, user=USER, pwd=PWD, host=DB_HOST, name=DB_NAME
) if DB_TYPE else 'sqlite:///' + os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    os.path.join(BASE_DIR, 'instance/development_app.db')
)

SQLALCHEMY_MIGRATE_REPO = os.environ.get(
    'SQLALCHEMY_MIGRATE_FOLDER', os.path.join(BASE_DIR, '..', 'instance/db_repository')
)
# Turn this off to reduce overhead
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
