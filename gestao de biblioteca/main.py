import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from view.main_ui import Ui_MainWindow

'''
from services.main_window_service import
'''


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
