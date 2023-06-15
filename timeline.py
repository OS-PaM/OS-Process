class Timeline:
    from pcb import PCB as __PCB
    from scheduler import Scheduler as __Scheduler

    time = 0
    __pid = 0
    __exe_time = 0
    __ready_queue: list[__PCB] = []

    def __init__(self, pcb_list: list[__PCB],
                 scheduler: __Scheduler):
        # TODO: 深拷贝? (可令 pcb_list 多次使用)
        from copy import deepcopy as __deepcopy

        self.pcb_list = __deepcopy(pcb_list)
        self.pcb_list.sort(
            key=lambda pcb: pcb.arrive_time)

        self.__scheduler = scheduler

    def step(self):
        from pcb import State as __State

        # TODO: 逻辑优化

        while True:
            time = self.time + self.__exe_time

            finish = True
            for pcb in self.pcb_list:
                if (time >= pcb.arrive_time and
                        pcb.state == __State.NONE):
                    pcb.state = __State.READY
                    pcb.pid = self.__pid
                    self.__pid += 1
                    self.__ready_queue.append(pcb)

                if pcb.state != __State.FINISH:
                    finish = False

            # TODO: 全部完成后的处理 (抛异常?)
            if not finish:
                self.__exe_time = self.__scheduler(
                    time, self.__ready_queue)

                for pcb in self.pcb_list:
                    # TODO: 计算 ran_time (或者继续交给 Scheduler)
                    if pcb.state == __State.RUNNING:
                        if pcb.start_time is None:
                            pcb.start_time = time
                            pcb.ran_time = 0

                        pcb.turnaround_time = time - pcb.start_time

                    if (pcb.state == __State.FINISH and
                            pcb in self.__ready_queue):
                        self.__ready_queue.remove(pcb)

                    if (pcb.state == __State.NONE and
                            time + self.__exe_time >= pcb.arrive_time):
                        self.__exe_time = pcb.arrive_time - time
                        break
                self.time = time
            else:
                break
        # TODO: 返回值优化?
        return self.time, self.pcb_list
