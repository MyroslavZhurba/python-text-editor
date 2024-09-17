import tkinter as tk
from app.menus.custom_menu import CustomMenu
import logging


class EditMenu(CustomMenu):
    """Class represents menu responsible for working with text."""
    def __init__(self, window, text_widget):
        super().__init__(window, text_widget)
        self.selected_text = ''

    def configure_menu(self, main_menu) -> None:
        edit_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Edit", menu=edit_menu)

        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator='Ctrl + C')
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator='Ctrl + V')
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator='Ctrl + X')
        edit_menu.add_command(label="Select All", command=self.select_all_text, accelerator='Ctrl + A')

        self.text_widget.bind('<Control-c>', self.copy_text)
        self.text_widget.bind('<Control-v>', self.paste_text)
        self.text_widget.bind('<Control-x>', self.cut_text)
        self.text_widget.bind('<Control-a>', self.select_all_text)

    def copy_text(self, event=None) -> None:
        if event:
            # If copying is done already via keyboard, copy the selected text
            self.selected_text = self.window.clipboard_get()
        else:
            try:
                self.text_widget.selection_get()
                self.selected_text = self.text_widget.selection_get()

                self.window.clipboard_clear()
                self.window.clipboard_append(self.selected_text)
            except tk.TclError:
                logging.info('Failed to copy - nothing is selected')

    def paste_text(self, event=None) -> None:
        if event:
            # If pasting is done already via keyboard, copy the pasted text
            self.selected_text = self.window.clipboard_get()
        elif self.selected_text:
            cursor_position = self.text_widget.index(tk.INSERT)
            self.text_widget.insert(cursor_position, self.selected_text)

    def cut_text(self, event=None) -> None:
        if event:
            # If cutting is done already via keyboard, copy the cutout text
            self.selected_text = self.window.clipboard_get()
        else:
            try:
                self.text_widget.selection_get()
                self.selected_text = self.text_widget.selection_get()
                self.text_widget.delete("sel.first", "sel.last")

                self.window.clipboard_clear()
                self.window.clipboard_append(self.selected_text)
            except tk.TclError:
                logging.info('Failed to cut - nothing is selected')

    def select_all_text(self, event=None) -> None:
        # Create a 'sel' tag which by default has a background color
        self.text_widget.tag_add('sel', '1.0', tk.END)
        # Jump to the end of the text
        self.text_widget.see(tk.END)
