import logging
import tkinter as tk
from tkinter import font
from app import config
from app.menus.custom_menu import CustomMenu
from app.status_bar import StatusBar


class ViewMenu(CustomMenu):
    """Class represents menu responsible for the app view"""
    def __init__(self, window, text_widget, status_bar: StatusBar, text_font: font.Font):
        super().__init__(window, text_widget)
        self.status_bar = status_bar
        self.status_bar_presence = tk.BooleanVar(value=True)
        self.text_font = text_font

    def configure_menu(self, main_menu) -> None:
        view_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="View", menu=view_menu)

        scale_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="Scale", menu=scale_menu)

        scale_menu.add_command(label="Up", command=self.scale_up, accelerator='Ctrl + plus')
        scale_menu.add_command(label="Down", command=self.scale_down, accelerator='Ctrl + minus')
        scale_menu.add_command(label="Restore default", command=self.restore_default_scale, accelerator='Ctrl + 0')

        view_menu.add_checkbutton(label="Status Bar", variable=self.status_bar_presence, command=self.show_status_bar)

        self.text_widget.bind('<Control-=>', self.scale_up)
        self.text_widget.bind('<Control-minus>', self.scale_down)
        self.text_widget.bind('<Control-0>', self.restore_default_scale)

    def scale_up(self, event=None) -> None:
        """Scale up the text widget by increasing font size"""
        if config.scale < 500:
            config.scale += 10
            diff = int(config.DEFAULT_FONT_SIZE / 10)
            config.current_font_size += diff

            self.text_font.config(size=config.current_font_size)
            self.status_bar.update_scale_number()
            logging.info(f'Current font size is set to {config.current_font_size}')
        else:
            logging.info('Was not able to scale up - max scale is reached')

    def scale_down(self, event=None) -> None:
        """Scale down the text widget by decreasing font size """
        if config.scale > 10:
            config.scale -= 10
            diff = int(config.DEFAULT_FONT_SIZE / 10)
            config.current_font_size -= diff

            self.text_font.config(size=config.current_font_size)
            self.status_bar.update_scale_number()
            logging.info(f'Current font size is set to {config.current_font_size}')
        else:
            logging.info('Was not able to scale down - min scale is reached')

    def restore_default_scale(self, event=None):
        """Set scale to default and resize font back to default size"""
        config.scale = 100
        config.current_font_size = config.DEFAULT_FONT_SIZE

        self.text_font.config(size=config.current_font_size)
        self.status_bar.update_scale_number()
        logging.info(f'Current font size is set to {config.current_font_size}')

    def show_status_bar(self) -> None:
        """Show or hide status bar"""
        if self.status_bar_presence.get():
            self.status_bar.show()
        else:
            self.status_bar.hide()
