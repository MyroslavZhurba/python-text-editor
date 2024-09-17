from ctypes import windll
import logging

# Fix issue with low resolution
windll.shcore.SetProcessDpiAwareness(1)

# Configure logging
logging.basicConfig(level=logging.INFO)

DEFAULT_WINDOW_TITLE = 'Text Editor - New File'
DEFAULT_FONT_FAMILY = 'Consolas'
DEFAULT_FONT_SIZE = 12

# Set which file types to look for when opening or saving as a file
DEFAULT_FILE_TYPES = [("Text Files", "*.txt"), ("All Files", "*.*")]

# Set default scale and font size
scale = 100
current_font_size = DEFAULT_FONT_SIZE

