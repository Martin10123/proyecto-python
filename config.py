import os
from dotenv import load_dotenv

load_dotenv()

FERRUM_URL = os.getenv('FERRUM_URL')

def get_users() -> list[tuple[str, str]]:
    """Retorna solo los usuarios que están completamente configurados."""
    users = []
    for i in range(1, 5):
        user = os.getenv(f'FERRUM_USER{i}')
        pwd  = os.getenv(f'FERRUM_PASS{i}')
        if user and pwd:
            users.append((user, pwd))
    return users