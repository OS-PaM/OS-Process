import gc
import sys

from PyQt5.QtWidgets import QMainWindow

from process_schedule.gui.ui.ui_main import Ui_MainWindow
from .gui_tool import check_algorithm, trans_html_info
from .input_dialog import in_dialog
from ..core import Timeline


class show_window(QMainWindow, Ui_MainWindow):
    scheduler = "fcfs"
    pcb_list = []
    timeline = None
    page = 0
    pc_bar_list = []
    pc_label_list = []
    start_html = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
                 + "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
                 + "p, li { white-space: pre-wrap; }\n" \
                 + "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
    state_html = str(start_html)

    def __init__(self):
        super(show_window, self).__init__()
        sys.excepthook = lambda ty, value, traceback: \
            [button.setEnabled(False) if button == self.change_button else button.setEnabled(True) for button in
             [self.start_button, self.change_button]]
        self.setupUi(self)
        self.start_button.clicked.connect(lambda: self.start_button_push())
        self.change_button.clicked.connect(lambda: self.change_button_push())
        self.pgup_button.clicked.connect(lambda: self.pgup_button_push())
        self.pgdn_button.clicked.connect(lambda: self.pgdn_button_push())
        self.actionFCFS.triggered.connect(lambda: self.fcfs_menu_push())
        self.actionSJF.triggered.connect(lambda: self.sjf_menu_push())
        self.actionSRTN.triggered.connect(lambda: self.srtn_menu_push())
        self.actionRR.triggered.connect(lambda: self.rr_menu_push())
        self.pc_bar_list.append(self.pc_bar_1)
        self.pc_bar_list.append(self.pc_bar_2)
        self.pc_bar_list.append(self.pc_bar_3)
        self.pc_bar_list.append(self.pc_bar_4)
        self.pc_bar_list.append(self.pc_bar_5)
        self.pc_label_list.append(self.pc_label_1)
        self.pc_label_list.append(self.pc_label_2)
        self.pc_label_list.append(self.pc_label_3)
        self.pc_label_list.append(self.pc_label_4)
        self.pc_label_list.append(self.pc_label_5)
        self.clear_state()
        self.state_text.setHtml(self.start_html)
        self.state_html = str(self.start_html)

    def start_button_push(self):
        self.clear_all()
        dialog = in_dialog()
        dialog()
        dialog.exec()
        self.pcb_list = dialog.get_pcb_list()
        if self.pcb_list:
            self.timeline = Timeline(self.pcb_list, check_algorithm(self.scheduler))
            self.clear_state()
            self.state_text.setHtml(self.start_html)
            self.change_button.setEnabled(True)
            self.state_html = str(self.start_html)
            self.start_button.setEnabled(False)
        self.change_bar()
        pass

    def change_button_push(self):
        if self.timeline is None or self.pcb_list == []:
            self.state_text.setText(" ---- 状态错误 请重新初始化 ---- ")
        else:
            now_data = self.timeline()
            info = trans_html_info(now_data[1])
            self.time_lcd.display(str(now_data[0]))
            self.pcb_list = now_data[1]
            self.state_html = info
            self.change_bar()
            self.state_text.setHtml(self.state_html)

    def pgup_button_push(self):
        self.page = self.page - 1
        self.change_bar()
        self.disable_button()
        pass

    def pgdn_button_push(self):
        self.page = self.page + 1
        self.change_bar()
        self.disable_button()
        pass

    def disable_button(self):

        if self.page == 0:
            self.pgup_button.setEnabled(False)
        else:
            self.pgup_button.setEnabled(True)

        if (self.page + 1) * 5 > len(self.pcb_list):
            self.pgdn_button.setEnabled(False)
        else:
            self.pgdn_button.setEnabled(True)

    def fcfs_menu_push(self):
        self.scheduler = "fcfs"
        pass
    def sjf_menu_push(self):
        self.scheduler = "sjf"
        pass
    def srtn_menu_push(self):
        self.scheduler = "srtn"
        pass
    def rr_menu_push(self):
        self.scheduler = "rr"
        pass

    def clear_all(self):
        self.clear_state()
        self.page = 0
        self.timeline = None
        self.time_lcd.display(0)
        gc.collect()

    def clear_state(self):
        i = 0
        while i < 5:
            self.pc_bar_list[i].setValue(0)
            self.pc_bar_list[i].setMaximum(100)
            self.pc_label_list[i].setText("N/A ")
            i = i + 1
        self.disable_button()

    def change_bar(self):
        self.clear_state()
        if self.page < int(len(self.pcb_list) / 5):
            max_num = 5
        else:
            max_num = len(self.pcb_list) % 5
        i = 0
        while i < max_num:
            pcb = self.pcb_list[self.page * 5 + i]
            if str(pcb.state) == "State.NONE":
                self.pc_label_list[i].setText("未入队")
                self.pc_bar_list[i].setRange(0, 0)
            else:
                self.pc_bar_list[i].setRange(0, pcb.run_time)
                self.pc_bar_list[i].setValue(pcb.ran_time)
                self.pc_label_list[i].setText("PID " + str(pcb.pid))
            i = i + 1
