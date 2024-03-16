#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading


class ScheduledTasksTimer:
    def __init__(self, interval, function):
        self.timer = threading.Timer(interval, function)
        self.timer.start()
        print("Timer initialized")

    def cancel(self):
        self.timer.cancel()
        print("Timer canceled")


class ScheduledTasks:
    def __init__(self):
        self.count = 0
        pass

    def scheduled_task_1(self):
        print(f"scheduled_task_1 {self.count}")
        self.count = self.count + 1

    def scheduled_task_2(self):
        print(f"scheduled_task_2 {self.count}")
        self.count = self.count + 1

