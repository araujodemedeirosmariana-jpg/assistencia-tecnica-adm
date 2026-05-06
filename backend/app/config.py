from datetime import timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "..", "database", "assistencia.db")
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

class Settings:
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    SECRET_KEY = "sua-chave-secreta-aqui-mude-em-producao"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
