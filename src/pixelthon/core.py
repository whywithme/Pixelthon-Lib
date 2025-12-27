import tkinter as tk
from tkinter import ttk
import ctypes
from .styles import configure_theme, COLORS

class PixelWindow:
    def __init__(self, title="Pixelthon App", width=500, height=600):
        # Включаем High DPI (четкость текста)
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass # Если это Linux или MacOS, пропускаем

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        
        # Применяем стили
        configure_theme(self.root)

        # Главный контейнер с отступами, чтобы элементы не липли к краям
        self.container = tk.Frame(self.root, bg=COLORS["bg"])
        self.container.pack(fill="both", expand=True, padx=30, pady=30)

    def add_label(self, text, size=12, bold=False):
        """Добавляет текст."""
        font_style = ("Segoe UI", size, "bold" if bold else "normal")
        lbl = ttk.Label(
            self.container, 
            text=text, 
            font=font_style, 
            background=COLORS["bg"], 
            foreground=COLORS["fg"]
        )
        lbl.pack(pady=(0, 15), anchor="w") # anchor="w" = выравнивание по левому краю
        return lbl

    def add_input(self, placeholder=""):
        """Добавляет поле ввода."""
        # Лайфхак: создаем фрейм, чтобы сделать красивую обводку или отступ
        entry = ttk.Entry(self.container, style="Pixel.TEntry")
        entry.pack(fill="x", pady=(0, 20), ipady=3) # ipady увеличивает высоту поля
        return entry

    def add_button(self, text, action=None):
        """Добавляет красивую кнопку."""
        btn = ttk.Button(
            self.container, 
            text=text, 
            command=action, 
            style="Pixel.TButton",
            cursor="hand2"
        )
        btn.pack(fill="x", pady=(10, 10))
        return btn
    
    def add_spacer(self, height=20):
        """Пустое пространство для разделения блоков."""
        spacer = tk.Frame(self.container, bg=COLORS["bg"], height=height)
        spacer.pack()

    def show(self):
        """Запускает приложение."""
        self.root.mainloop()