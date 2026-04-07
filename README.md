# 🤖 Bot Ferrum - Automatización de Plataforma Educativa

Un bot automatizado que simula interacciones humanas en la plataforma **Ferrum** del Tecnológico Comfenalco, permitiendo automatizar tareas repetitivas de navegación, acceso a cursos y publicación de comentarios en foros educativos.

---

## 📋 Descripción General

Este proyecto utiliza **Playwright** para automatizar procesos en la plataforma Ferrum. El bot es capaz de:

✅ **Autenticarse** con múltiples usuarios  
✅ **Navegar** a cursos específicos  
✅ **Acceder** a evaluaciones formativas  
✅ **Participar** en foros de discusión  
✅ **Publicar comentarios** automáticamente  
✅ **Detectar y adaptar** automáticamente el idioma de la plataforma (Español/Inglés)  

---

## 🎯 Funcionalidades Principales

### 1. **Autenticación Multi-usuario**
- Soporta hasta 4 usuarios diferentes configurados en `.env`
- Selección interactiva del usuario al iniciar
- Gestión segura de credenciales

### 2. **Navegación Inteligente**
- Detección automática del idioma de la plataforma
- Adaptación de selectores según idioma activo
- Navegación fluida de Cursos → Electiva III → Evaluación Formativa → Foros

### 3. **Interacción Humana**
- Delays aleatorios para simular comportamiento humano
- Esperas inteligentes por elementos de la página
- Manejo robusto de timeouts

### 4. **Soporte Multiidioma**
El bot detecta automáticamente si la plataforma está en:
- 🇪🇸 **Español** - usa selectores en español
- 🇬🇧 **Inglés** - usa selectores en inglés

---

## 🔧 Requisitos

- **Python 3.8+**
- **Playwright** - automatización del navegador
- **python-dotenv** - gestión de variables de entorno

---

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/proyecto-python-main.git
cd proyecto-python-main
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Instalar navegadores de Playwright
```bash
playwright install chromium
```

### Flujo de ejecución
1. Se abre una ventana del navegador (Chrome)
2. Selecciona un usuario de la lista
3. Se realiza login automático
4. Navega a "Mis Cursos" / "My Courses"
5. Abre el curso "ELECTIVA III"
6. Accede a "Evaluación Formativa" / "Formative Assessment"
7. Entra al foro "¿Eres un robot?" / "Are you a robot?"
8. Publica un comentario automáticamente

---

## 📁 Estructura del Proyecto

```
proyecto-python-main/
├── main.py                 # Punto de entrada principal
├── config.py              # Configuración y carga de .env
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── .env                  # Credenciales (NO incluir en git)
└── bot/
    ├── __init__.py
    ├── auth.py           # Autenticación y login
    ├── navigation.py     # Navegación entre páginas
    ├── forum.py          # Funciones del foro
    └── utils.py          # Utilidades y funciones auxiliares
```

---

## 📚 Módulos

### `config.py`
- Carga variables de entorno desde `.env`
- Proporciona URL de Ferrum
- Gestiona múltiples usuarios

### `bot/auth.py`
- Realiza login en la plataforma
- Maneja credenciales de usuarios

### `bot/navigation.py`
- Navega a "Mis Cursos"
- Abre cursos específicos
- Accede a evaluaciones
- **Soporte multiidioma incluido**

### `bot/forum.py`
- Accede a foros de discusión
- Publica comentarios automáticamente
- **Adapta botones según el idioma**

### `bot/utils.py`
- **`detect_language(page)`** - Detecta idioma actual (ES/EN)
- **`safe_click()`** - Click seguro con espera
- **`safe_fill()`** - Relleno seguro de campos
- **`human_delay()`** - Delays aleatorios

---

## 👨‍💻 Autores

- ** VALERIN CARDENAS VILLALOBO
- ** JOSE COLON GAMARRA
- ** SHARICK DE LAS AGUAS
- ** MARTIN SIMARRA
