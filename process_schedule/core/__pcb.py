from dataclasses import dataclass as __dataclass
from enum import Enum as __Enum
from enum import unique as __unique


@__unique
class State(__Enum):
    from enum import auto as __auto

    NONE = __auto()
    READY = __auto()
    RUNNING = __auto()
    FINISH = __auto()


@__dataclass
class PCB:
    arrive_time: int
    run_time: int
    ran_time: int = -1
    pid: int = -1
    start_time: int = -1
    last_time: int = -1
    end_time: int = -1
    turnaround_time: int = -1
    state: State = State.NONE

    def __init__(self, arrive_time: int, run_time: int):
        if arrive_time < 0:
            raise ValueError(f"arrive_time 为负数: {arrive_time}")
        if run_time <= 0:
            raise ValueError(f"run_time 小于或等于 0: {run_time}")

        self.arrive_time = arrive_time
        self.run_time = run_time

    @property
    def remain_time(self):
        return self.run_time - self.ran_time

    def ready(self, pid=-1):
        self.state = State.READY

        if pid >= 0 and self.pid < 0:
            self.turnaround_time = 0
            self.ran_time = 0

            self.pid = pid

    def run(self, time: int):
        self.state = State.RUNNING
        if self.start_time < 0:
            self.start_time = time
        self.last_time = time
        return self.remain_time

    def finish(self, time: int):
        self.state = State.FINISH
        self.end_time = time

    def is_arrive(self, time: int):
        return time >= self.arrive_time

    def update_turnaround_time(self, time: int):
        self.turnaround_time = time - self.arrive_time

    @property
    def is_none(self):
        return self.state == State.NONE

    @property
    def is_ready(self):
        return self.state == State.READY

    @property
    def is_running(self):
        return self.state == State.RUNNING

    @property
    def is_finish(self):
        return self.state == State.FINISH
