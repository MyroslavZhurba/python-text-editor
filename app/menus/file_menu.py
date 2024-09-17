import tkinter as tk
from tkinter import filedialog
from app import config
from app.menus.custom_menu import CustomMenu
import logging


class FileMenu(CustomMenu):
    """Class represents menu responsible for working with files"""
    def __init__(self, window, text_widget):
        super().__init__(window, text_widget)
        self.current_file_path = None

    def configure_menu(self, main_menu) -> None:
        file_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New", command=self.new_file, accelerator='Ctrl + N')
        file_menu.add_command(label="Open", command=self.open_file, accelerator='Ctrl + O')
        file_menu.add_command(label="Save", command=self.save_file, accelerator='Ctrl + S')
        file_menu.add_command(label="Save As", command=self.save_as_file, accelerator='Ctrl + Shift + S')
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)

        self.text_widget.bind_all('<Control-n>', self.new_file)
        self.text_widget.bind('<Control-o>', self.open_file)
        self.text_widget.bind('<Control-s>', self.save_file)
        self.text_widget.bind_all('<Control-S>', self.save_as_file)

    def new_file(self, event=None) -> None:
        """Erase all previous text to create new file"""
        self.text_widget.delete(1.0, tk.END)
        self.window.title('Text Editor - New File')
        self.current_file_path = None

        logging.info('New file is started')

    def open_file(self, event=None) -> None:
        """Open existing file and change window title"""
        file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=config.DEFAULT_FILE_TYPES)
        if file_path:
            self.window.title(f"Text Editor - {file_path}")
            self.text_widget.delete(1.0, tk.END)
            with open(file_path, 'r') as file:
                self.text_widget.insert(tk.INSERT, file.read())

            self.current_file_path = file_path
            logging.info('Existing file is opened')

    def save_file(self, event=None) -> None:
        """Save current changes in existing file"""
        if self.current_file_path:
            with open(self.current_file_path, 'w') as file:
                file.write(self.text_widget.get(1.0, tk.END))

            logging.info('Changes are saved')
        else:
            self.save_as_file()

    def save_as_file(self, event=None) -> None:
        """Save current changes as new file and change window title"""
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=config.DEFAULT_FILE_TYPES)

        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

            self.window.title(f"Text Editor - {file_path}")
            self.current_file_path = file_path
            logging.info('Changes are saved')

    def exit(self) -> None:
        """Close the app"""
        self.window.destroy()
        logging.info('App is closed')
