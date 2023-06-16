from .__scheduler import Scheduler as __Scheduler


class FCFS(__Scheduler):
    from ..pcb import PCB as __PCB

    def __call__(self, time: int,
                 ready_queue: list[__PCB]):

        pcb = ready_queue[0]
        if pcb.is_running:
            return pcb.remain_time

        if pcb.is_ready:
            return pcb.run(time)
