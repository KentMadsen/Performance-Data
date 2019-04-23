import pipeline
import counter

class Telemetry:
    """  """
    __slots__ = ['x', 'y', 'title', 'description', 'x_type', 'y_type', 'pipeline', 'append_counter']

    def __init__(self):
        self.title = ""
        self.description = ""

        self.x_type = ""
        self.y_type = ""

        self.pipeline = None
        self.set_pipeline(pipeline.Pipeline())

        self.append_counter = counter.Counter()

        return

    @classmethod
    def initialise(cls, path, filename, extension):
        cls.pipeline.initialise(path, filename, extension)
        return

    @classmethod
    def append(cls, x_value, y_value):
        cls.__append_to_x(value=x_value)
        cls.__append_to_y(value=y_value)

        cls.append_counter.increment()

        return

    @classmethod
    def __out_trigger(cls):
        if cls.append_counter.getValue() == 1024:
            cls.append_counter.reset()
            cls.__out()

        return

    @classmethod
    def remove(cls, index):
        cls.__remove_element_at_x(index)
        cls.__remove_element_at_y(index)
        return

    # Accessors
    @classmethod
    def get_pipeline(cls):
        return cls.pipeline

    @classmethod
    def set_pipeline(cls, value):
        if not isinstance(value, telemetry_pipeline.Pipeline):
            raise ValueError("")
        cls.pipeline = value

    @classmethod
    def get_x_type(cls):
        return cls.x_type

    @classmethod
    def get_y_type(cls):
        return cls.y_type

    @classmethod
    def set_x_type(cls, value):
        if not isinstance(value, str):
            raise ValueError("")

        cls.x_type = value

    @classmethod
    def set_y_type(cls, value):
        if not isinstance(value, str):
            raise ValueError("")

        cls.y_type = value

    @classmethod
    def set_title(cls, value):
        if not isinstance(value, str):
            raise ValueError("")

        cls.title = value

    @classmethod
    def get_title(cls):
        return cls.title

    @classmethod
    def set_description(cls, value):
        if not isinstance(value, str):
            raise ValueError("")

        cls.description = value

    @classmethod
    def get_description(cls):
        return cls.description

    # Base Functions
    @classmethod
    def __get_x(cls):
        return cls.x

    @classmethod
    def __get_y(cls):
        return cls.y

    #
    @classmethod
    def __set_x(cls, values):
        if not isinstance(values, list):
            raise ValueError("")

        for i in range(len(values)):
            v = values[i]
            if not isinstance(v, int):
                raise ValueError("")

        cls.x = values

    @classmethod
    def __set_y(cls, values):
        if not isinstance(values, list):
            raise ValueError("")

        for i in range(len(values)):
            v = values[i]
            if not isinstance(v, int):
                raise ValueError("")

        cls.y = values

    #
    @classmethod
    def __append_to_x(cls, value):
        if not isinstance(value, int):
            raise ValueError("")
        cls.x.append(value)

    @classmethod
    def __append_to_y(cls, value):
        if not isinstance(value, int):
            raise ValueError("")
        cls.y.append(value)

    #
    @classmethod
    def __remove_element_at_x(cls, value_index):
        if len(cls.x) > value_index:
            del cls.x[value_index]
        return

    @classmethod
    def __remove_element_at_y(cls, value_index):
        if len(cls.y) > value_index:
            del cls.y[value_index]
        return

    @classmethod
    def size(cls):
        a = len(cls.x)
        b = len(cls.y)

        if a == b:
            return a
        else:
            raise ValueError('')

    @classmethod
    def print(cls):
        print("title: " + cls.get_title())
        print("description: " + cls.get_description())

        print("x label type: " + cls.get_x_type())
        print(cls.__get_x())
        print("y label type: " + cls.get_y_type())
        print(cls.__get_y())

        return
