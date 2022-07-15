class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kura:testingu@localhost/smilecookingu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
