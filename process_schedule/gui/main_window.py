from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from process_schedule.gui.ui.ui_main import Ui_MainWindow
from .input_dialog import in_dialog
from ..core import Timeline


class show_window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(show_window, self).__init__()
        self.setupUi(self)
        self.start_button.clicked.connect(lambda :self.start_button_push())

    def start_button_push(self):
        dialog = in_dialog()
        dialog.exec()
        pass
