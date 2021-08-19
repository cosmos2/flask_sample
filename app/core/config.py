import os
import redis

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'bad secret')
    DEBUG = False

    # DB
    SQLALCHEMY_DATABASE_URI = f"postgresql://developer:devpassword@localhost:5432/developer"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url('redis://localhost:25100')

    # cache
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = '25100'
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = 'redis://localhost:25100'
    CACHE_DEFAULT_TIMEOUT = 500

    PER_PAGE = 10


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    develop=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY
