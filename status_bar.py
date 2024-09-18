import tkinter as tk
import config
import logging


class StatusBar:
    """
    Class represents status bar on the bottom of the window.
    It contains current scale of the text widget and number of written characters
    """
    def __init__(self, window: tk.Tk, text_widget: tk.Text):
        self.window = window
        self.text_widget = text_widget

        # Create frame to hold status bar
        self.frame = tk.Frame(window)
        self.frame.grid(row=1, column=0, sticky='ew', padx=20)

        self.char_count = tk.Label(self.frame, anchor=tk.W)
        self.char_count.pack(side=tk.LEFT)

        self.scale = tk.Label(self.frame, text='100%', anchor=tk.E)
        self.scale.pack(side=tk.RIGHT)

        # After every keypress update the char count
        self.text_widget.bind('<KeyRelease>', self.update_char_count)

    def update_char_count(self, event=None) -> None:
        char_count = len(self.text_widget.get('1.0', tk.END)) - 1
        self.char_count.config(text=f"{char_count} characters")

    def show(self) -> None:
        self.frame.grid(row=1, column=0, sticky='ew', padx=20)
        logging.info('Status bar is shown')

    def hide(self) -> None:
        self.frame.grid_forget()
        logging.info('Status bar is hidden')

    def update_scale_number(self) -> None:
        current_scale = config.scale
        self.scale.config(text=f"{current_scale}%")
        logging.info(f'Current scale is set to {current_scale}')
