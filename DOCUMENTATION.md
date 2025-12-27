# Pixelthon Full Documentation 📘

**[ 🇺🇸 English Documentation ](#english)** | **[ 🇷🇺 Русская документация ](#russian)**

---

<a name="english"></a>
## 🇺🇸 Pixelthon API Reference

Pixelthon is designed to be a wrapper around Python's `tkinter`. It abstracts away the layout management (`pack`/`grid`) and styling configurations, providing a clean, declarative API.

### 1. Main Class: `PixelWindow`

The core of the library. It represents the application window.

#### Initialization

    app = PixelWindow(title="My App", width=500, height=600)

**Parameters:**
*   `title` (str): The text displayed in the window title bar.
*   `width` (int): The initial width of the window in pixels. Default is 500.
*   `height` (int): The initial height of the window in pixels. Default is 600.

**Behavior:**
*   Automatically enables High DPI awareness on Windows systems (prevents blurry text).
*   Applies the dark theme (`#1e1e2e` background).
*   Creates a main container frame with padding.

---

### 2. Widget Methods

These methods are called on the `PixelWindow` instance to add elements to the screen. Elements are added vertically, from top to bottom.

#### `add_label(text, size=12, bold=False)`
Adds a text label to the window.

*   **Parameters:**
    *   `text` (str): The string to display.
    *   `size` (int, optional): Font size. Default: 12.
    *   `bold` (bool, optional): If `True`, applies bold font weight. Default: `False`.
*   **Returns:** `tkinter.ttk.Label` object.
*   **Usage:** Use for headers, instructions, or static text.

#### `add_input(placeholder="")`
Adds a single-line text entry field.

*   **Parameters:**
    *   `placeholder` (str, optional): Currently reserved for future updates (custom placeholder logic).
*   **Returns:** `tkinter.ttk.Entry` object.
*   **Important:** You must assign this return value to a variable to retrieve user input later.
*   **Retrieving Data:** Call `.get()` on the returned object.
    
    Example:
    
        user_input = app.add_input()
        print(user_input.get())

#### `add_button(text, action=None)`
Adds a full-width styled button.

*   **Parameters:**
    *   `text` (str): The text displayed on the button.
    *   `action` (callable, optional): The function to be executed when the button is clicked. Pass the function name **without parentheses**.
*   **Returns:** `tkinter.ttk.Button` object.

#### `add_spacer(height=20)`
Adds an invisible block to create vertical space between elements.

*   **Parameters:**
    *   `height` (int, optional): The height of the empty space in pixels. Default: 20.
*   **Returns:** `tkinter.Frame` object (transparent).

---

### 3. Execution Control

#### `show()`
Starts the application's main event loop.

*   **Parameters:** None.
*   **Description:** This method blocks the execution of the script until the window is closed by the user. It must be the last line of your GUI setup code.

---

### 4. Full Example

    from pixelthon import PixelWindow

    def calculate():
        # Get values from input fields
        val = entry.get()
        print(f"Processing: {val}")

    # Initialize
    app = PixelWindow("Documentation Example", 400, 300)

    # Header
    app.add_label("Data Processor", size=18, bold=True)
    
    # Form
    app.add_label("Enter Value:")
    entry = app.add_input()
    
    # Spacing and Action
    app.add_spacer(15)
    app.add_button("Run Process", action=calculate)

    # Start
    app.show()

---
---

<a name="russian"></a>
## 🇷🇺 Документация Pixelthon API

Pixelthon разработана как обертка над стандартной библиотекой `tkinter`. Она скрывает сложность управления макетами (`pack`/`grid`) и настройку стилей, предоставляя чистый, декларативный API.

### 1. Основной класс: `PixelWindow`

Ядро библиотеки. Представляет собой окно приложения.

#### Инициализация

    app = PixelWindow(title="Мое приложение", width=500, height=600)

**Параметры:**
*   `title` (str): Текст, отображаемый в заголовке окна.
*   `width` (int): Начальная ширина окна в пикселях. По умолчанию 500.
*   `height` (int): Начальная высота окна в пикселях. По умолчанию 600.

**Поведение:**
*   Автоматически включает поддержку High DPI на Windows (предотвращает размытость текста).
*   Применяет темную тему (фон `#1e1e2e`).
*   Создает главный контейнер с внутренними отступами.

---

### 2. Методы добавления виджетов

Эти методы вызываются у экземпляра `PixelWindow` для добавления элементов на экран. Элементы добавляются вертикально, сверху вниз.

#### `add_label(text, size=12, bold=False)`
Добавляет текстовую метку (лейбл) в окно.

*   **Параметры:**
    *   `text` (str): Текст для отображения.
    *   `size` (int, необязательно): Размер шрифта. По умолчанию: 12.
    *   `bold` (bool, необязательно): Если `True`, делает шрифт жирным. По умолчанию: `False`.
*   **Возвращает:** Объект `tkinter.ttk.Label`.
*   **Использование:** Используется для заголовков, инструкций или статического текста.

#### `add_input(placeholder="")`
Добавляет однострочное поле для ввода текста.

*   **Параметры:**
    *   `placeholder` (str, необязательно): Зарезервировано для будущих обновлений (плейсхолдеры).
*   **Возвращает:** Объект `tkinter.ttk.Entry`.
*   **Важно:** Вы должны сохранить возвращаемое значение в переменную, чтобы позже получить введенные данные.
*   **Получение данных:** Вызовите метод `.get()` у сохраненного объекта.
    
    Пример:
    
        user_input = app.add_input()
        # Позже, при нажатии кнопки:
        print(user_input.get())

#### `add_button(text, action=None)`
Добавляет стилизованную кнопку во всю ширину контейнера.

*   **Параметры:**
    *   `text` (str): Текст на кнопке.
    *   `action` (callable, необязательно): Функция, которая будет выполнена при клике. Передавайте имя функции **без скобок**.
*   **Возвращает:** Объект `tkinter.ttk.Button`.

#### `add_spacer(height=20)`
Добавляет невидимый блок для создания вертикального пространства между элементами.

*   **Параметры:**
    *   `height` (int, необязательно): Высота пустого пространства в пикселях. По умолчанию: 20.
*   **Возвращает:** Объект `tkinter.Frame` (прозрачный).

---

### 3. Управление выполнением

#### `show()`
Запускает главный цикл событий приложения.

*   **Параметры:** Нет.
*   **Описание:** Этот метод блокирует выполнение скрипта до тех пор, пока окно не будет закрыто пользователем. Это должна быть последняя строка вашего кода настройки интерфейса.

---

### 4. Полный пример

    from pixelthon import PixelWindow

    def calculate():
        # Получаем значение из поля ввода
        val = entry.get()
        print(f"Обработка значения: {val}")

    # Инициализация
    app = PixelWindow("Пример документации", 400, 300)

    # Заголовок
    app.add_label("Обработчик данных", size=18, bold=True)
    
    # Форма
    app.add_label("Введите значение:")
    entry = app.add_input()
    
    # Отступ и Кнопка
    app.add_spacer(15)
    app.add_button("Запустить", action=calculate)

    # Старт
    app.show()
