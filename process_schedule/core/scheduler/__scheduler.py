from abc import ABC as __ABC


class Scheduler(__ABC):
    from abc import abstractmethod as __abstractmethod

    from .. import PCB as __PCB

    @__abstractmethod
    def __call__(self, time: int,
                 ready_queue: list[__PCB]) -> int:
        """
        **调度算法的具体实现**

        ----

        需要做的操作:

            1. 更新 运行状态

                + 运行使用 ``pcb.run()``, 会自动更新 ``pcb.last_time``
                + 挂起使用 ``pcb.ready()``, 无需传参
                + 完成会自动处理

            2. 调整 就绪队列

                TODO: 封装 调整函数 或 自动调整

            3. 返回 剩余时间

                + 无特殊需求返回 ``pcb.remain_time`` 即可
                + 特殊需求如 ``RR`` 算法请自行处理

        ----

        :param time: 当前时间
        :param ready_queue: 就绪队列

        :return: 剩余时间
        """
        pass
