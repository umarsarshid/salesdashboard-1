class Config:
    # Base configuration
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    # Development specific configurations

class ProductionConfig(Config):
    DEBUG = False
    # Production specific configurations
