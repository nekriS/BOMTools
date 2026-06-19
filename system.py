import sys
from PySide6.QtWidgets import QApplication, QMessageBox

def show_standalone_error(title, message):
    # Initialize the Qt application lifecycle
    app = QApplication.instance()
    if not app:
        # Only create a new one if it doesn't exist
        app = QApplication(sys.argv)
    
    # Show error window. Setting parent to None makes it a top-level window.
    QMessageBox.critical(None, title, message)

def log(text):
    print(text)
    show_standalone_error("Обнаружена ошибка!", 
                          f"""В процессе выполнения обнаружена ошибка:\n                          
{text}
                          """)