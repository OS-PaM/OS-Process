from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from process_schedule.core import PCB
from process_schedule.gui.ui.ui_dialog import Ui_Dialog


class in_dialog(QDialog, Ui_Dialog):
    pcb_list = []
    pid: int = 0

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

    def __call__(self, *args, **kwargs):
        self.pcb_list = []
        super.__call__()

    def next_button_click(self):
        if self.pid != len(self.pcb_list):  # pid 和 pcb_list长度不一致时 证明重新进行了初始化 需要清空
            self.pcb_list = []
        arr_time = self.arr_line.text()
        run_time = self.run_line.text()
        if arr_time != "" and run_time != "" and int(run_time):
            self.pid = self.pid + 1
            pcb = PCB(int(self.arr_line.text()), int(self.run_line.text()))
            self.pcb_list.append(pcb)
            self.pid_label.setText("程序 " + str(self.pid) + "\t上一项 (" + "程序 " + str(self.pid - 1) + ") 已记录")
        else:
            self.pid_label.setText("程序 " + str(self.pid) + "\t内容不能为 Null or 0")
            self.setWindowTitle("内容不能为 Null or 0")
        pass

    def exec_(self):
        return self.pcb_list

    def enter_button_click(self):
        self.hide()
        pass

    def get_pcb_list(self):
        return self.pcb_list
