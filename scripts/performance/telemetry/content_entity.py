class PipelineEntity:
    """ """
    __slots__ = ['value', 'header_name', 'loaded']

    def __init__(self):
        self.value = 0
        self.header_name = 0

        self.loaded = False
        return

    def get_value(self):
        return self.value

    def set_value(self, value_parameter):
        self.value = value_parameter

    def get_header_name(self):
        return self.header_name

    def set_header_name(self, value_parameter):
        self.header_name = value_parameter

    def get_loaded(self):
        return self.loaded

    def set_loaded(self, value_parameter):
        self.loaded = value_parameter
