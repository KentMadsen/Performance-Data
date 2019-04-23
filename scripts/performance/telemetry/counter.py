default_increase = 1

class Counter:
    """ """
    __slots__ = ['value']

    def __init__(self):
        self.value = 0

    def increment(self):
        global default_increase
        self.increase(default_increase)
        return

    def increase(self, size):
        self.value = self.value + size
        return

    def decrement(self):
        global default_increase
        self.decrease(default_increase)
        return

    def decrease(self, size):
        self.value = self.value - size
        return

    def setValue(self, valueSize):
        if isinstance(self.value, int):
            self.value = valueSize
        else:
            raise ValueError("")

    def getValue(self):
        return self.value

    def reset(self):
        self.value = 0

    def print(self):
        return str(self.value)
