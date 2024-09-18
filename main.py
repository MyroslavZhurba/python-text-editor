import logging
from text_editor import TextEditor

my_text_editor = TextEditor()
# Configure main menu to have access to more functionality
my_text_editor.configure_main_menu()

if __name__ == '__main__':
    try:
        my_text_editor.start_app()
    except KeyboardInterrupt:
        logging.info('App is closed')
