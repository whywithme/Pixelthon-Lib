import tkinter as tk
from tkinter import ttk

# Палитра Pixelthon
COLORS = {
    "bg": "#1e1e2e",          # Темно-серый фон (почти черный)
    "fg": "#cdd6f4",          # Мягкий белый текст
    "accent": "#89b4fa",      # Акцентный синий
    "button": "#585b70",      # Цвет кнопок
    "button_hover": "#45475a",# Цвет кнопок при наведении
    "success": "#a6e3a1",     # Зеленый
    "input_bg": "#313244"     # Фон полей ввода
}

FONT_MAIN = ("Segoe UI", 11)
FONT_BOLD = ("Segoe UI", 11, "bold")

def configure_theme(root):
    style = ttk.Style()
    style.theme_use('clam')  # 'clam' дает лучший контроль над цветами

    # 1. Настройка фона окна
    root.configure(bg=COLORS["bg"])

    # 2. Настройка общих стилей виджетов
    style.configure(
        ".", 
        background=COLORS["bg"], 
        foreground=COLORS["fg"], 
        font=FONT_MAIN
    )

    # 3. Настройка Кнопки (PixelButton)
    style.configure(
        "Pixel.TButton",
        background=COLORS["accent"],
        foreground="#1e1e2e",  # Темный текст на светлой кнопке
        borderwidth=0,
        focuscolor=COLORS["bg"],
        font=FONT_BOLD,
        padding=(20, 10)  # Широкие отступы
    )
    style.map("Pixel.TButton",
        background=[('active', COLORS["fg"]), ('pressed', COLORS["button"])]
    )

    # 4. Настройка Поля ввода (PixelInput)
    style.configure(
        "Pixel.TEntry",
        fieldbackground=COLORS["input_bg"],
        foreground=COLORS["fg"],
        borderwidth=0,
        padding=10,
        insertcolor=COLORS["fg"] # Цвет курсора
    )