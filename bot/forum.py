from playwright.sync_api import Page
from bot.utils import safe_click, human_delay, detect_language

COMENTARIO = "No soy un robot"

def entrar_foro(page: Page) -> None:
    selector = 'span.instancename:has-text("¿Eres un robot?")'
    
    safe_click(page, selector)
    page.wait_for_load_state('networkidle')
    human_delay()
    
    print(f"Dentro del foro")

def publicar_comentario(page: Page) -> None:
    lang = detect_language(page)
    
    if lang == 'es':
        selector_add = 'a[href="#collapseAddForm"], a:has-text("Agregar tema de discusión")'
    else:
        selector_add = 'a[href="#collapseAddForm"], a:has-text("Add discussion topic")'
    
    safe_click(page, selector_add)
    human_delay(1000, 1800)

    page.wait_for_selector('#id_subject', timeout=8000)
    page.fill('#id_subject', COMENTARIO)
    human_delay(500, 1000)

    editor = page.locator('#id_messageeditable')
    editor.wait_for(timeout=8000)
    editor.click()
    human_delay(300, 600)
    editor.fill(COMENTARIO)
    human_delay(800, 1500)

    if lang == 'es':
        selector_submit = 'input[name="submitbutton"][value="Publicar en el foro"]'
    else:
        selector_submit = 'input[name="submitbutton"][value="Post to forum"]'
    
    safe_click(page, selector_submit)
    page.wait_for_load_state('networkidle')
    
    print(f"Comentario publicado")