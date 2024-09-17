import tkinter as tk
from abc import ABC, abstractmethod


class CustomMenu(ABC):
    """Model for all the menus"""
    def __init__(self, window: tk.Tk, text_widget: tk.Text):
        self.window = window
        self.text_widget = text_widget

    @abstractmethod
    def configure_menu(self, main_menu: tk.Menu) -> None:
        """Adds buttons and sets bindings"""
        pass
