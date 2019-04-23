import system_break

class Business:
    """ """
    __slots__ = ['system_break']

    def __init__(self):
        self.system_break = system_break.SystemBreak(1)

        return

    def initialise(self):

        return

    def execute(self):
        self.system_break.run()
        return

    def deinitialise(self):

        return
