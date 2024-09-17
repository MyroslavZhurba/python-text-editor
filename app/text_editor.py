import tkinter as tk
from tkinter import font
import logging
from app import config
from app.menus.file_menu import FileMenu
from app.menus.edit_menu import EditMenu
from app.menus.view_menu import ViewMenu
from app.status_bar import StatusBar


class TextEditor:
    """
    Class represents text editor app. To use its full functionality
    main menu needs to be configured before starting the app.
    """
    def __init__(self):
        # Configure main window
        self.window = tk.Tk()
        self.window.title(config.DEFAULT_WINDOW_TITLE)
        self.window.geometry('1800x1000')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Configure frame for text and scrollbar widgets
        self.frame = tk.Frame(self.window)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.main_menu = tk.Menu(self.window)
        self.window.config(menu=self.main_menu)

        # Configure text widget with undo functionality
        self.text_font = font.Font(family=config.DEFAULT_FONT_FAMILY, size=config.DEFAULT_FONT_SIZE)
        self.text_widget = tk.Text(self.frame, font=self.text_font, wrap=tk.WORD, undo=True)
        self.text_widget.grid(row=0, column=0, sticky='nsew', padx=(20, 0), pady=(20, 0))

        # Configure text scrolling
        self.scroll_bar = tk.Scrollbar(self.frame)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.text_widget.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text_widget.yview)

        # Configure correct widget displaying inside the frame
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.status_bar = StatusBar(self.window, self.text_widget)

    def configure_main_menu(self) -> None:
        """Add different menus to the main menu."""
        my_file_menu = FileMenu(self.window, self.text_widget)
        my_edit_menu = EditMenu(self.window, self.text_widget)
        my_view_menu = ViewMenu(self.window, self.text_widget, self.status_bar, self.text_font)

        my_file_menu.configure_menu(self.main_menu)
        my_edit_menu.configure_menu(self.main_menu)
        my_view_menu.configure_menu(self.main_menu)

    def start_app(self) -> None:
        logging.info('App is started')
        self.window.mainloop()
