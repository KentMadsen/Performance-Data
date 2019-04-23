class PipelineHeader:
    """ """
    __slots__ = ['row_index', 'header_name']

    def __init__(self):
        self.row_index = 0
        self.header_name = "None"
        return

    def get_header_name(self):
        return self.header_name

    def set_header_name(self, value):
        self.header_name = value

    def get_row_index(self):
        return self.row_index

    def set_row_index(self, value):
        self.row_index = value
