class Config:
    DEBUG = False
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kura:testingu@localhost/smilecookingu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
