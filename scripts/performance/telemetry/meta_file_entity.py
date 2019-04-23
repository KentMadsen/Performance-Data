import os

class FileMetaEntity():
    __slots__ = ['path', 'state', 'file_name', 'file_extension']

    def __init__(self):
        self.path = None

        self.file_name = None
        self.file_extension = None

        self.state = None

        self.file = None

        self.set_state(0)

        return

    # Accessor
    def get_file(self):
        return self.file

    def set_file(self, value):
        self.file = value

    def get_path(self):
        return self.path

    def get_name(self):
        return self.file_name

    def get_extension(self):
        return self.file_extension

    def get_full_path(self):
        value = str(self.get_path()) + "\\" + str(self.get_name()) + ("." + str(self.get_extension()))
        return value

    def set_path(self, path_value):
        self.path = path_value

    def set_name(self, name_value):
        self.file_name = name_value

    def set_extension(self, ext_value):
        self.file_extension = ext_value

    def set_state(self, value):
        if value > 4:
            raise ValueError("")

        if value == 0:
            self.state = "none"
            return

        if value == 1:
            self.state = "created"
            return

        if value == 2:
            self.state = "append"
            return

        if value == 3:
            self.state = "overwrite"
            return

        if value == 4:
            self.state = "reading"
            return

        return

        def get_state(self):
            return self.state

    #
    def is_file_present(self):
        if os.path.isfile(self.get_full_path()):
            return True

        return False
