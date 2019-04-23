import business

class Application:
    """ """

    __slots__ = ['Continue', 'Business']

    def __init__(self):
        self.Continue = True
        self.Business = business.Business()

    def initialise(self):
        self.Business.initialise()
        return

    def execute(self):
        while self.get_continue():
            self.Business.execute()

        return

    def completion(self):
        self.Business.completion()
        return

    def set_continue(self, value):
        self.Continue = value

    def get_continue(self):
        return self.Continue
