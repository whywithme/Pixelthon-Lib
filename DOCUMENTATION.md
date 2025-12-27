# Pixelthon Framework Documentation 📘

**Current Version:** 0.1.0
**License:** MIT

**[ 🇺🇸 English Documentation ](#english)** | **[ 🇷🇺 Русская документация ](#russian)**

---

<a name="english"></a>
# 🇺🇸 Pixelthon - English Documentation

## 1. Introduction

Pixelthon is a high-level wrapper around Python's standard `tkinter` library. Its primary goal is to lower the barrier to entry for creating Graphical User Interfaces (GUIs) while enforcing modern design principles by default.

**Core Philosophies:**
1.  **Declarative Syntax:** The user defines *what* they want (Input, Button), not *how* to place it (Grid, Pack coordinates).
2.  **Modern Defaults:** Dark mode, padding, and High DPI scaling are applied automatically.
3.  **Linear Layout:** The library utilizes a vertical stack layout strategy, ideal for forms, installers, and utility tools.

---

## 2. Installation & Setup

### 2.1. Installing from PyPI (Wheel)
If you have the compiled `.whl` file:

```
    pip install dist/pixelthon-0.1.0-py3-none-any.whl
```

### 2.2. Developer Mode
If you are modifying the library source code, install it in editable mode. Navigate to the folder containing `pyproject.toml` and run:

```
    pip install -e .
```

### 2.3. Requirements
*   Python 3.7 or higher.
*   Standard libraries: `tkinter`, `ctypes` (Windows only).
*   OS: Windows 10/11 (Optimized), macOS, Linux.

---

## 3. Architecture & Internal Logic

Pixelthon abstracts the `tkinter.Tk` root window and the `ttk` styling engine.

### The Layout Engine
Instead of exposing `grid()` or `pack()`, Pixelthon creates a central container frame (`self.container`) with padding. All widgets added via `add_*` methods are packed into this container using `pack(fill='x')`. This ensures responsive width resizing while maintaining a vertical flow.

### High DPI Awareness
On initialization, the library attempts to call `ctypes.windll.shcore.SetProcessDpiAwareness(1)`.
*   **On Windows:** This prevents blurred text on scaling > 100%.
*   **On Linux/macOS:** This block is safely ignored (caught by try/except).

---

## 4. API Reference

### 4.1. The Main Class: `PixelWindow`

```python
    from pixelthon import PixelWindow
    app = PixelWindow(title="App Name", width=500, height=600)
```

**Arguments:**
*   `title` (str): Sets the window title in the OS taskbar/header.
*   `width` (int): Initial window width in pixels.
*   `height` (int): Initial window height in pixels.

---

### 4.2. UI Components (Widgets)

All methods below are members of the `PixelWindow` class.

#### `add_label(text, size=12, bold=False)`
Renders a text block.

*   **Arguments:**
    *   `text` (str): The content string.
    *   `size` (int): Font size (Segoe UI). Defaults to 12.
    *   `bold` (bool): Toggle bold font weight.
*   **Returns:** `tkinter.ttk.Label` instance.
*   **Styling:** Uses the background color `#1e1e2e` and foreground `#cdd6f4`.

#### `add_input(placeholder="")`
Renders a styled text entry field.

*   **Arguments:**
    *   `placeholder` (str): Reserved for future placeholder implementation.
*   **Returns:** `tkinter.ttk.Entry` instance.
*   **Technical Note:** To access the data entered by the user, you must store the return value of this method and call `.get()` on it later.

#### `add_button(text, action=None)`
Renders a CTA (Call To Action) button.

*   **Arguments:**
    *   `text` (str): Button label.
    *   `action` (callable): A reference to a Python function. Do NOT call the function (e.g., use `my_func`, not `my_func()`).
*   **Returns:** `tkinter.ttk.Button` instance.
*   **Styling:** Accent color `#89b4fa`, hover color `#45475a`. Cursor changes to `hand2` on hover.

#### `add_spacer(height=20)`
Renders an invisible frame to push content apart.

*   **Arguments:**
    *   `height` (int): Height in pixels.
*   **Returns:** `tkinter.Frame` instance.

#### `show()`
Starts the `mainloop`.

*   **Description:** Transfers control to the GUI event loop. Code after this method will not execute until the window is closed.

---

## 5. Design System (Theme)

Pixelthon uses a hardcoded "Cosmic Dark" palette defined in `styles.py`.

| Component | Color Hex | Description |
| :--- | :--- | :--- |
| **Background** | `#1e1e2e` | Deep grey/black |
| **Text** | `#cdd6f4` | Soft white |
| **Accent** | `#89b4fa` | Light Blue (Buttons) |
| **Input Bg** | `#313244` | Lighter grey for fields |
| **Success** | `#a6e3a1` | Green (reserved) |

**Fonts:**
The library prioritizes **Segoe UI** (Windows standard). If unavailable on Linux/Mac, Tkinter falls back to the system default sans-serif font.

---

## 6. Comprehensive Example

```python
    from pixelthon import PixelWindow

    # 1. Define Logic
    def submit_form():
        user = entry_user.get()
        pwd = entry_pass.get()
        
        if user and pwd:
            print(f"Logging in as {user}...")
            # Here you would add your backend logic
        else:
            print("Error: Fields cannot be empty")

    # 2. Init Window
    app = PixelWindow("Enterprise Login", 400, 500)

    # 3. Build UI
    app.add_label("Welcome Back", size=24, bold=True)
    app.add_label("Please sign in to continue")
    
    app.add_spacer(30)
    
    app.add_label("Username")
    entry_user = app.add_input()
    
    app.add_label("Password")
    entry_pass = app.add_input() # Note: In real apps, use show="*" for passwords
    
    app.add_spacer(30)
    
    app.add_button("Secure Login", action=submit_form)

    # 4. Run
    app.show()
```

---

## 7. Troubleshooting

**Error: `ImportError: cannot import name 'PixelWindow'`**
*   **Cause:** The library is installed incorrectly or `__init__.py` is empty.
*   **Fix:** Ensure `src/pixelthon/__init__.py` contains `from .core import PixelWindow` and run `pip install .` again.

**Issue: Text looks tiny on 4K screens**
*   **Cause:** DPI awareness failed.
*   **Fix:** Ensure you are running Python 3.7+ on Windows 10/11. On Linux, check your generic Tkinter scaling settings (`export TK_LIBRARY` etc).

---
---

<a name="russian"></a>
# 🇷🇺 Pixelthon - Русская документация

## 1. Введение

Pixelthon — это высокоуровневая обертка над стандартной библиотекой Python `tkinter`. Основная цель — снизить порог входа для создания графических интерфейсов (GUI), предоставляя современный дизайн по умолчанию.

**Философия библиотеки:**
1.  **Декларативный синтаксис:** Пользователь определяет *что* он хочет создать (Поле ввода, Кнопку), а не *как* это разместить (координаты Grid, Pack).
2.  **Современные стандарты:** Тёмная тема, отступы и поддержка высокого разрешения (High DPI) включены автоматически.
3.  **Линейный макет:** Библиотека использует стратегию вертикального стека (элементы идут друг за другом сверху вниз), что идеально подходит для форм, инсталлеров и утилит.

---

## 2. Установка и Настройка

### 2.1. Установка из файла (Wheel)
Если у вас есть скомпилированный файл `.whl`:

```
    pip install dist/pixelthon-0.1.0-py3-none-any.whl
```

### 2.2. Режим разработчика
Если вы меняете исходный код библиотеки, установите её в редактируемом режиме. Перейдите в папку с `pyproject.toml` и выполните:

```
    pip install -e .
```

### 2.3. Требования
*   Python 3.7 или выше.
*   Стандартные библиотеки: `tkinter`, `ctypes` (только для Windows).
*   ОС: Windows 10/11 (Оптимизировано), macOS, Linux.

---

## 3. Архитектура и Внутренняя логика

Pixelthon абстрагирует корневое окно `tkinter.Tk` и движок стилизации `ttk`.

### Движок макетов (Layout Engine)
Вместо того чтобы заставлять пользователя учить `grid()` или `pack()`, Pixelthon создает центральный фрейм-контейнер (`self.container`) с внутренними отступами. Все виджеты, добавляемые через методы `add_*`, упаковываются в этот контейнер, используя `pack(fill='x')`. Это гарантирует, что элементы будут растягиваться по ширине окна, сохраняя вертикальный поток.

### Поддержка High DPI (Четкость)
При инициализации библиотека пытается вызвать системную функцию Windows: `ctypes.windll.shcore.SetProcessDpiAwareness(1)`.
*   **На Windows:** Это предотвращает размытие текста при масштабировании экрана > 100%.
*   **На Linux/macOS:** Этот блок игнорируется (обрабатывается через try/except), используется стандартный рендеринг системы.

---

## 4. Справочник API

### 4.1. Главный класс: `PixelWindow`

```python
    from pixelthon import PixelWindow
    app = PixelWindow(title="Имя приложения", width=500, height=600)
```

**Аргументы:**
*   `title` (str): Устанавливает заголовок окна в панели задач ОС.
*   `width` (int): Начальная ширина окна в пикселях.
*   `height` (int): Начальная высота окна в пикселях.

---

### 4.2. Компоненты UI (Виджеты)

Все методы ниже вызываются у экземпляра класса `PixelWindow`.

#### `add_label(text, size=12, bold=False)`
Отрисовывает блок текста.

*   **Аргументы:**
    *   `text` (str): Содержимое строки.
    *   `size` (int): Размер шрифта (используется Segoe UI). По умолчанию 12.
    *   `bold` (bool): Переключатель жирного начертания.
*   **Возвращает:** Экземпляр `tkinter.ttk.Label`.
*   **Стиль:** Использует цвет фона `#1e1e2e` и цвет текста `#cdd6f4`.

#### `add_input(placeholder="")`
Отрисовывает стилизованное поле ввода текста.

*   **Аргументы:**
    *   `placeholder` (str): Зарезервировано для будущей реализации подсказок внутри поля.
*   **Возвращает:** Экземпляр `tkinter.ttk.Entry`.
*   **Техническое примечание:** Чтобы получить данные, введенные пользователем, вы должны сохранить возвращаемое значение этого метода в переменную, а затем вызвать у неё `.get()`.

#### `add_button(text, action=None)`
Отрисовывает кнопку действия (CTA).

*   **Аргументы:**
    *   `text` (str): Надпись на кнопке.
    *   `action` (callable): Ссылка на Python-функцию. НЕ вызывайте функцию (передавайте `my_func`, а не `my_func()`).
*   **Возвращает:** Экземпляр `tkinter.ttk.Button`.
*   **Стиль:** Акцентный цвет `#89b4fa`, при наведении `#45475a`. Курсор меняется на "руку" (hand2).

#### `add_spacer(height=20)`
Отрисовывает невидимый блок для разделения контента.

*   **Аргументы:**
    *   `height` (int): Высота в пикселях.
*   **Возвращает:** Экземпляр `tkinter.Frame`.

#### `show()`
Запускает `mainloop`.

*   **Описание:** Передает управление циклу событий GUI. Код, написанный после этого метода, не будет выполнен, пока окно не закроется.

---

## 5. Дизайн-система (Тема)

Pixelthon использует жестко заданную палитру "Cosmic Dark", определенную во внутреннем модуле `styles.py`.

| Компонент | HEX Код | Описание |
| :--- | :--- | :--- |
| **Фон** | `#1e1e2e` | Глубокий темно-серый/черный |
| **Текст** | `#cdd6f4` | Мягкий белый |
| **Акцент** | `#89b4fa` | Светло-синий (Кнопки) |
| **Фон Input** | `#313244` | Светло-серый для полей |
| **Успех** | `#a6e3a1` | Зеленый (зарезервировано) |

**Шрифты:**
Библиотека отдает приоритет **Segoe UI** (стандарт Windows). Если он недоступен (Linux/Mac), Tkinter использует системный шрифт без засечек по умолчанию.

---

## 6. Полный пример использования
```python
    from pixelthon import PixelWindow

    # 1. Логика приложения
    def submit_form():
        user = entry_user.get()
        pwd = entry_pass.get()
        
        if user and pwd:
            print(f"Вход выполнен для: {user}")
            # Здесь могла бы быть ваша логика проверки пароля
        else:
            print("Ошибка: Поля не могут быть пустыми")

    # 2. Инициализация окна
    app = PixelWindow("Корпоративный портал", 400, 500)

    # 3. Построение интерфейса
    app.add_label("С возвращением", size=24, bold=True)
    app.add_label("Пожалуйста, авторизуйтесь")
    
    app.add_spacer(30)
    
    app.add_label("Имя пользователя")
    entry_user = app.add_input()
    
    app.add_label("Пароль")
    entry_pass = app.add_input() 
    # Примечание: В реальных приложениях используйте show="*" для паролей
    
    app.add_spacer(30)
    
    app.add_button("Безопасный вход", action=submit_form)

    # 4. Запуск
    app.show()
```
---

## 7. Устранение неполадок

**Ошибка: `ImportError: cannot import name 'PixelWindow'`**
*   **Причина:** Библиотека установлена неправильно, либо файл `__init__.py` пуст.
*   **Решение:** Убедитесь, что `src/pixelthon/__init__.py` содержит строку `from .core import PixelWindow` и выполните `pip install .` снова.

**Проблема: Текст выглядит очень мелким на 4K экране**
*   **Причина:** Не сработала High DPI осведомленность.
*   **Решение:** Убедитесь, что вы используете Python 3.7+ на Windows 10/11. На Linux проверьте настройки масштабирования Tkinter (`export TK_LIBRARY` и т.д.).
