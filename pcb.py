from enum import Enum as __Enum
from enum import unique as __unique

from datclass import dataclass as __dataclass


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
    pid: int | None = None
    # TODO: -1? None?
    start_time: int | None = None
    turnaround_time: int | None = None
    ran_time: int | None = None
    state: State = State.NONE
