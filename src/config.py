import os

POSTGRES_USER = os.environ.get('POSTGRES_USER',False)
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', False)
POSTGRES_DB = os.environ.get('POSTGRES_DB', False)
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', False)
if POSTGRES_USER and POSTGRES_PASSWORD and POSTGRES_DB and POSTGRES_HOST:
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
else:
    BASEDIR = os.path.abspath(os.path.dirname(__name__))
    DATABASE_URL = SQLITE_DB = "sqlite:///" + os.path.join(BASEDIR, "db.sqlite")

class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())
    if "sqlite://" in DATABASE_URL:
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE", "America/Anchorage")
    BROKER_URL = os.getenv("BROKER_URL", "redis://localhost")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost")
    CELERY_SEND_SENT_EVENT = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

# return active config
available_configs = dict(development=DevelopmentConfig, production=ProductionConfig)
selected_config = os.getenv("FLASK_ENV", "production")
config = available_configs.get(selected_config, "production")
