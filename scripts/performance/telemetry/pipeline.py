# Internal Files
import counter

import content_entity
import header_entity

import meta_file_entity

width_standard = 2
height_standard = 5

class Pipeline:
    """ The Pipeline for the telemetry class. It's job is to act, as a pipeline.
        For retrieving (import) and storing data (export). Essentially the Persistence layer for the system. """

    __slots__ = [ 'entity', 'file', 'headers', 'model', 'file', 'format']

    def __init__(self):
        self.entity = meta_file_entity.FileMetaEntity()

        self.format = None

        self.headers = []

        return

    # Function
    def initialise(self, path, filename, ext):
        self.entity.set_path(path)
        self.entity.set_name(filename)
        self.entity.set_extension(ext)

        if self.entity.is_file_present():
            self.read_document_content()
            #self.append_mode()
            return
        else:
            #self.create_mode()

            return

    def read_document_content(self):

        return

    # Accessor
    def get_file(self):
        return self.file

    def set_file(self, value):
        self.file = value

    def get_entity(self):
        return self.entity

    def set_entity(self, value):
        self.entity = value

    def get_format(self):
        return self.format

    def set_format(self, value):
        self.format = value
