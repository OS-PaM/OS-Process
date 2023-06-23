import sys
from pprint import pprint
from sys import stderr

from PyQt5 import QtWidgets

from process_schedule.core import PCB, Timeline
from process_schedule.core.scheduler import FCFS, SJF, RR
from process_schedule.gui.main_window import show_window


def my_pprint(obj):
    pprint(obj)
    print()


def doc_out():
    pcb_list = [PCB(1, 3), PCB(0, 24), PCB(2, 3)]
    # pcb_list = [PCB(0, 24), PCB(27, 3)]
    fcfs_timeline = Timeline(pcb_list, FCFS())

    try:
        # TODO: 结果可视化 (GUI?)
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
        my_pprint(fcfs_timeline())
    except OverflowError as e:
        print(e, file=stderr)


if __name__ == '__main__':
    # doc_out()

    app = QtWidgets.QApplication(sys.argv)
    main_ui = show_window()
    main_ui.show()
    sys.exit(app.exec_())
