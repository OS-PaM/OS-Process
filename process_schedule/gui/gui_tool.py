from process_schedule.core.scheduler import SJF, FCFS


def check_algorithm(string):
    if string == "fcfs":
        return FCFS()
    if string == "sjf":
        return SJF()
    pass


def trans_html_info(pcb_list):
    info = ""
    style = "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
    for pcb in pcb_list:

        pid = str(pcb.pid)
        state = str(pcb.state)
        arrive_time = str(pcb.arrive_time)
        ran_time = str(pcb.ran_time)
        turnaround_time = str(pcb.turnaround_time)
        run_time = str(pcb.run_time)
        start_time = str(pcb.start_time)
        last_time = str(pcb.last_time)

        if start_time == "-1":
            start_time = "None"
        if last_time == "-1":
            last_time = "None"

        if state == "State.NONE":
            info = info + "<p>  PID: " + "未入队" + ";</p>\n" + \
                   "<p " + style + ">-  状态: " + "未入队" + ";</p>\n" + \
                   "<p " + style + ">-  总到达时间: " + arrive_time + ";</p>\n" + \
                   "<p " + style + ">-  运行所需时间: " + run_time + ";</p>\n" + \
                   "<p " + style + ">-----------------------------------</p>\n"
        else:
            info = info + "<p>  PID: " + pid + ";</p>\n" + \
                   "<p " + style + ">-  状态: " + state + ";</p>\n" + \
                   "<p " + style + ">-  总到达时间: " + arrive_time + ";</p>\n" + \
                   "<p " + style + ">-  已运行时间: " + ran_time + ";</p>\n" + \
                   "<p " + style + ">-  当前周转时间: " + turnaround_time + ";</p>\n" + \
                   "<p " + style + ">-  运行所需时间: " + run_time + ";</p>\n" + \
                   "<p " + style + ">-  开始运行时间点: " + start_time + ";</p>\n" + \
                   "<p " + style + ">-  最新运行时间点: " + last_time + ";</p>\n" + \
                   "<p " + style + ">-----------------------------------</p>\n"

    return info
