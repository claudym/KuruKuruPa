class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{kura}:{testingu}@localhost/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
