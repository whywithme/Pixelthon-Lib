# Pixelthon 🎨

**[ 🇺🇸 English Version ](#english)** | **[ 🇷🇺 Русская версия ](#russian)**

---

<a name="english"></a>
## 🇺🇸 English Description

Pixelthon is a Python library for creating modern, beautiful GUIs in seconds.
Forget about complex Tkinter boilerplates and the gray Windows 95 look. Pixelthon handles the styling automatically.

### ⚡ Features

- 🌑 **Dark Mode by Default**: A professional dark color scheme right out of the box.
- 👁 **High DPI**: Automatic support for crisp text on Windows 10/11 and 4K monitors.
- 🚀 **Minimal Code**: No need to worry about `root`, `pack`, `grid`, or `mainloop`. Just add your elements.
- 🐍 **Pythonic**: Clean, declarative syntax.

### 📦 Installation

If you have built the wheel file locally:

    pip install dist/pixelthon-0.1.0-py3-none-any.whl

Or, if you are developing inside the project folder:

    pip install .

### 🚀 Quick Start

Here is all you need to create a functional app:

    from pixelthon import PixelWindow

    # Function to handle button click
    def show_message():
        name = name_field.get()
        print(f"Hello, {name}!")

    # 1. Create the window
    app = PixelWindow("My First App", width=400, height=350)

    # 2. Add content
    app.add_label("System Login", size=20, bold=True)
    app.add_spacer(10)

    app.add_label("Enter your name:")
    name_field = app.add_input()

    app.add_spacer(20)
    app.add_button("Login", action=show_message)

    # 3. Run the app
    app.show()

### 📚 API Documentation

*   `PixelWindow(title, width, height)`: Creates the main window.
*   `app.add_label(text, size=12, bold=False)`: Adds a text label.
*   `app.add_input()`: Adds an input field. Returns the object (use `.get()` to read).
*   `app.add_button(text, action=None)`: Adds a button. `action` is the function to call.
*   `app.add_spacer(height=20)`: Adds vertical space.
*   `app.show()`: Starts the application loop.

---

<a name="russian"></a>
## 🇷🇺 Описание на русском

Pixelthon — это библиотека Python для создания современного и красивого графического интерфейса (GUI) за считанные секунды.
Забудьте о сложном коде Tkinter и сером дизайне из 90-х. Pixelthon делает всё красиво автоматически.

### ⚡ Особенности

- 🌑 **Тёмная тема по умолчанию**: Профессиональная цветовая схема "из коробки".
- 👁 **High DPI**: Автоматическая поддержка четкости шрифтов на Windows 10/11 и 4K мониторах.
- 🚀 **Минимум кода**: Не нужно знать про `root`, `pack`, `grid` или `mainloop`. Вы просто добавляете элементы.
- 🐍 **В стиле Python**: Чистый и понятный синтаксис.

### 📦 Установка

Если вы собрали wheel-файл локально:

    pip install dist/pixelthon-0.1.0-py3-none-any.whl

Или, если вы находитесь в папке с проектом:

    pip install .

### 🚀 Быстрый старт

Всё, что нужно для создания рабочей программы с кнопкой и полем ввода:

    from pixelthon import PixelWindow

    # Функция, которая сработает при нажатии
    def show_message():
        name = name_field.get()
        print(f"Привет, {name}!")

    # 1. Создаем окно
    app = PixelWindow("Мое первое приложение", width=400, height=350)

    # 2. Добавляем контент
    app.add_label("Вход в систему", size=20, bold=True)
    app.add_spacer(10)

    app.add_label("Введите ваше имя:")
    name_field = app.add_input()

    app.add_spacer(20)
    app.add_button("Войти", action=show_message)

    # 3. Запускаем
    app.show()

### 📚 Документация API

*   `PixelWindow(title, width, height)`: Создает главное окно приложения.
*   `app.add_label(text, size=12, bold=False)`: Добавляет текстовую надпись.
*   `app.add_input()`: Добавляет поле ввода. Возвращает объект (используйте `.get()` для чтения).
*   `app.add_button(text, action=None)`: Добавляет кнопку. `action` — имя функции для вызова.
*   `app.add_spacer(height=20)`: Добавляет пустой отступ по вертикали.
*   `app.show()`: Запускает цикл приложения.

---

## 📄 License / Лицензия

MIT License. Free to use for personal and commercial projects.
Свободно для использования в личных и коммерческих проектах.
