from .__scheduler import Scheduler as __Scheduler


class RR(__Scheduler):
    from .. import PCB as __PCB

    tmp_remain_time = None
    tmp_run_pcb = None
    state = False

    def __call__(self, time: int,
                 ready_queue: list[__PCB]):

        time_block = 3  # 时间片

        if self.state:  # state 上次是否有执行程序
            for i,pcb in enumerate(ready_queue):
                if pcb.is_running:
                    run_pcb = pcb
                    ready_queue.pop(i)    # 运行的程序还没有运行完 从队列里弹出
                    ready_queue.append(run_pcb)     # 重新装入到就绪队列的末尾
                    final_remain_time = max((self.tmp_remain_time - time_block), 0)
                    if run_pcb == self.tmp_run_pcb and run_pcb.remain_time > final_remain_time:
                        return_time = run_pcb.remain_time - final_remain_time   # 如果上一次执行未满时间片 因新进入了PCB 而进入了算法检查 就继续执行剩余时间
                        return return_time
                    else:
                        run_pcb.ready()
                        self.state = False
                    break

        now_pcb = ready_queue[0]    # 没有未执行完时间片的程序 就直接按队列顺序执行
        self.state = True
        self.tmp_remain_time = now_pcb.remain_time
        self.tmp_run_pcb = now_pcb
        if now_pcb.is_running:
            return min(now_pcb.remain_time,time_block)
        else:
            return min(now_pcb.run(time),time_block)
        pass
