from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from config import FERRUM_URL, get_users
from bot.auth import login
from bot.navigation import ir_a_mis_cursos, entrar_electiva_iii, entrar_evaluacion_formativa
from bot.forum import entrar_foro, publicar_comentario

def elegir_usuario() -> tuple[str, str]:
    users = get_users()
    if not users:
        raise ValueError("No hay usuarios configurados en el .env")

    print("\n Selecciona el usuario:")
    for i, (user, _) in enumerate(users, 1):
        print(f"  {i}. {user}")

    while True:
        try:
            sel = int(input("\nNúmero de usuario: "))
            if 1 <= sel <= len(users):
                return users[sel - 1]
            print("Selección fuera de rango.")
        except ValueError:
            print("Ingresa un número válido.")

def run_bot(username: str, password: str) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_context().new_page()
        try:
            page.goto(FERRUM_URL)
            login(page, username, password)
            ir_a_mis_cursos(page)
            entrar_electiva_iii(page)
            entrar_evaluacion_formativa(page)
            entrar_foro(page)
            publicar_comentario(page)

            print("\n Flujo completado.")
            input("Presiona Enter para cerrar...")
        except PlaywrightTimeoutError as e:
            print(f" Timeout: {e}")
        except Exception as e:
            print(f" Error: {e}")
        finally:
            browser.close()

if __name__ == '__main__':
    username, password = elegir_usuario()
    run_bot(username, password)