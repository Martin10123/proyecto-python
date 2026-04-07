from playwright.sync_api import Page
from bot.utils import safe_click, human_delay, detect_language

def ir_a_mis_cursos(page: Page) -> None:
    lang = detect_language(page)
    
    if lang == 'es':
        selector = 'a.nav-link[title="Cursos"]'
    else:
        selector = 'a.nav-link[title="Courses"]'
    
    safe_click(page, selector)
    page.wait_for_load_state('networkidle')
    human_delay()
    
    print(f"En Mis Cursos")

def entrar_electiva_iii(page: Page) -> None:
    safe_click(page, 'a:has(span:has-text("ELECTIVA III (CLASE 2651)"))')
    page.wait_for_load_state('networkidle')
    human_delay()
    print("Dentro de Electiva III")

def entrar_evaluacion_formativa(page: Page) -> None:
    selector = 'div.card-header[title="Evaluación Formativa"]'
    
    safe_click(page, selector)
    page.wait_for_load_state('networkidle')
    human_delay()
    
    print(f"En Evaluación Formativa")