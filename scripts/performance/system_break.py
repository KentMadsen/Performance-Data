import time

class SystemBreak:
    """"""
    __slots__ = ['time']

    def __init__(self, wait):
        self.time = wait
        return

    def run(self):
        time.sleep(self.get_time())
        return

    def set_time(self, value):
        self.time = value

    def get_time(self):
        return self.time
