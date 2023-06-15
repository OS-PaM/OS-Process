from pcb import PCB
from scheduler import FCFS
from timeline import Timeline

if __name__ == '__main__':
    pcb_list = [PCB(1, 3), PCB(0, 24)]
    fcfs_timeline = Timeline(pcb_list, FCFS())

    # TODO: 结果可视化 (GUI?)
    print(fcfs_timeline.step())
    print(fcfs_timeline.step())
    print(fcfs_timeline.step())
    print(fcfs_timeline.step())
    print(fcfs_timeline.step())
