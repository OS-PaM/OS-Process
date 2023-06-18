class Timeline:
    from . import PCB as __PCB
    from .scheduler import Scheduler as __Scheduler

    time = 0
    __pid = 0
    __run_time = 0
    __is_finish = False
    __ready_queue: list[__PCB] = []

    def __init__(self, pcb_list: list[__PCB],
                 scheduler: __Scheduler):
        from copy import deepcopy as __deepcopy

        self.pcb_list = __deepcopy(pcb_list)
        self.pcb_list.sort(
            key=lambda pcb: pcb.arrive_time)

        self.__scheduler = scheduler

    def __finish(self):
        if self.__is_finish:
            raise OverflowError('所有 PCB 均已运行完成')

    def __call__(self):
        self.time += self.__run_time

        self.__finish()
        self.__is_finish = True

        for pcb in self.pcb_list:
            # 进入就绪队列
            if (pcb.is_none and
                    pcb.is_arrive(self.time)):
                pcb.ready(self.__pid)
                self.__pid += 1
                self.__ready_queue.append(pcb)

            if not pcb.is_finish:
                # 更新列表完成状态
                self.__is_finish = False

                if not pcb.is_none:
                    # 更新周转时间
                    pcb.update_turnaround_time(self.time)

                    if pcb.is_running:
                        # 更新运行时间
                        pcb.ran_time += self.__run_time
                        # 标记完成并移除
                        if pcb.remain_time <= 0:
                            pcb.finish(self.time)
                            self.__ready_queue.remove(pcb)

        self.__finish()

        if self.__ready_queue:
            # 执行调度算法
            self.__run_time = self.__scheduler(
                self.time, self.__ready_queue)

        # 跳过空白时间
        for pcb in self.pcb_list:
            if (pcb.is_none and
                    pcb.is_arrive(
                        self.time + self.__run_time)):
                self.__run_time = (
                    pcb.arrive_time - self.time)
                break

        # TODO: 返回值优化?
        return self.time, self.pcb_list
