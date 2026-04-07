from playwright.sync_api import Page
from bot.utils import safe_fill, safe_click, human_delay

def login(page: Page, username: str, password: str) -> None:
    """Completa el flujo de autenticación."""
    safe_fill(page, 'input[name="username"]', username)
    safe_fill(page, 'input[name="password"]', password)
    safe_click(page, 'button.btn-login[type="submit"]')
    page.wait_for_load_state('networkidle')
    human_delay()
    print(f"Login exitoso: {username}")