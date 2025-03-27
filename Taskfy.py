from task_manager.SetupWindow import mainWindowWidget
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindowWidget()
    window.show()
    sys.exit(app.exec())
