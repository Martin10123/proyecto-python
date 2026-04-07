import time
import random
from playwright.sync_api import Page

def human_delay(min_ms: int = 600, max_ms: int = 1800) -> None:
    """Pausa aleatoria para simular comportamiento humano."""
    time.sleep(random.uniform(min_ms, max_ms) / 1000)

def detect_language(page: Page) -> str:
    """Detecta el idioma actual de la página.
    
    Retorna: 'es' para español, 'en' para inglés
    """
    try:
        lang_text = page.locator('span.langdesc').first.text_content()
        if lang_text and 'Español' in lang_text:
            return 'es'
        return 'en'
    except:
        try:
            html_lang = page.locator('html').get_attribute('lang')
            return html_lang.split('-')[0] if html_lang else 'es'
        except:
            return 'es'

def safe_click(page: Page, selector: str, timeout: int = 10000) -> None:
    """Espera a que el elemento exista y luego hace clic."""
    page.wait_for_selector(selector, timeout=timeout)
    human_delay()
    page.click(selector)

def safe_fill(page: Page, selector: str, text: str, timeout: int = 10000) -> None:
    """Espera a que el campo exista y luego lo rellena."""
    page.wait_for_selector(selector, timeout=timeout)
    human_delay()
    page.fill(selector, text)