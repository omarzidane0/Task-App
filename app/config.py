class Config:
    SECRET_KEY = "testing"
    JWT_SECRET_KEY = "your-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    JWT_ACCESS_TOKEN_EXPIRES = False