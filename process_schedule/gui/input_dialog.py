from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from process_schedule.core import Timeline, PCB
from process_schedule.gui.ui.ui_dialog import Ui_Dialog


class in_dialog(QDialog, Ui_Dialog):
    pcb_list = []
    pid: int

    def __init__(self):
        super(in_dialog, self).__init__()
        self.setupUi(self)
        self.pid = 0
        reg = QRegExp('[0-9]+$')
        validator = QRegExpValidator()
        validator.setRegExp(reg)
        self.run_line.setValidator(validator)
        self.arr_line.setValidator(validator)
        self.pushButton_2.clicked.connect(self.next_button_click)
        self.enter_button.clicked.connect(self.enter_button_click)
        pass

    def next_button_click(self):
        arr_time = self.arr_line.text()
        run_time = self.run_line.text()
        if arr_time != "" and run_time != "" and int(run_time):
            self.pid = self.pid + 1
            pcb = PCB(self.arr_line.text(), self.run_line.text())
            self.pcb_list.append(pcb)
            self.pid_label.setText("PID " + str(self.pid) + "\t上一项 (" + "PID " + str(self.pid - 1) + ") 已记录")
        else:
            self.pid_label.setText("PID " + str(self.pid) + "\t内容不能为 Null or 0")
            self.setWindowTitle("内容不能为 Null or 0")
        pass

    def enter_button_click(self):
        self.hide()
        pass
