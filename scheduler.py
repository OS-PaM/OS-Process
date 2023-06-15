from abc import ABC as __ABC


class Scheduler(__ABC):
    from abc import abstractmethod as __abstractmethod

    from pcb import PCB as __PCB

    # TODO: 更大的 skip_time ?
    def __init__(self, skip_time: int = 999):
        """
        构造方法

        可根据需求自行扩充子类参数列表, 如 RR 算法的 时间片大小

        :param skip_time: 当没有操作可做时 (就绪队列为空?),
                          要跳过的时间. 默认 `999`.
        """
        super().__init__()
        self.skip_time = skip_time

    # TODO: 优化逻辑
    @__abstractmethod
    def __call__(self, time: int,
                 ready_queue: list[__PCB]) -> int:
        """
        调度算法的具体实现

        需要做的操作:
            1. 更新 ran_time
            2. 更新进程状态
            3. 返回 剩余时间 (若无操作, 返回 skip_time)

        :param time: 当前时间
        :param ready_queue: 就绪队列
        :return: 剩余时间
        """
        pass


class FCFS(Scheduler):
    from pcb import PCB as __PCB

    
    def __call__(self, time: int,
                 ready_queue: list[__PCB]) -> int:
        from pcb import State as __State

        for pcb in ready_queue:
            if pcb.state == __State.RUNNING:
                pcb.ran_time = time - pcb.start_time
                if pcb.ran_time >= pcb.run_time:
                    pcb.state = __State.FINISH

            if time >= pcb.arrive_time:
                if pcb.state == __State.READY:
                    pcb.state = __State.RUNNING
                    return pcb.run_time
                if pcb.state == __State.RUNNING:
                    return pcb.run_time - pcb.ran_time

        return self.skip_time
