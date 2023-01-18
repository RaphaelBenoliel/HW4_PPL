

def make_class(attributes, base_class=None):
    """
    Create a new class object with the given attributes and base class.
    :param attributes: A dictionary of attributes for the class
    :param base_class: Optional base class to inherit from
    :return: A new class object
    """
    def get_value(name):
        """
        Get the value of an attribute of the class or its base class
        :param name: The name of the attribute
        :return: The value of the attribute
        """
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        """
        Set the value of an attribute of the class
        :param name: The name of the attribute
        :param value: The value of the attribute
        """
        attributes[name] = value

    def new(*args):
        """
        Initialize a new instance of the class
        :param args: Arguments to pass to the __init__ method
        :return: A new instance of the class
        """
        return init_instance(cls, *args)

    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls


def init_instance(cls, *args):

    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance


def make_instance(cls):
    """
    Create a new instance of the given class
    :param cls: The class to create an instance of
    :return: A new instance of the class
    """
    attributes = {}

    def get_value(name):
        """
        Get the value of an attribute of the instance
        :param name: The name of the attribute
        :return: The value of the attribute
        """
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        """
        Set the value of an attribute of the instance
        :param name: The name of the attribute
        :param value: The value of the attribute
        """
        attributes[name] = value

    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_method(value, instance):
    """
    Bind a method to an instance
    :param value: The method to bind
    :param instance: The instance to bind the method to
    :return: The bound method
    """
    if callable(value):
        def method(*args):
            """
            Call the bound method with the given arguments
            :param args: The arguments to pass to the method
            :return: The result of calling the method
            """
            return value(instance, *args)

        return method
    else:
        return value


def make_date_class():
    """
    Create a new class for representing dates.
    :return: A new class for representing dates
    """
    def __init__(self, year, month, day):
        """
        Initialize a new date instance with the given year, month, and day.
        :param year: The year of the date
        :param month: The month of the date
        :param day: The day of the date
        """
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)

    return make_class({'__init__': __init__})


def make_time_class():
    """
    Create a new class for representing times.
    :return: A new class for representing times
    """
    def __init__(self, hour, minute):
        """
        Initialize a new time instance with the given hour and minute.
        :param hour: The hour of the time
        :param minute: The minute of the time
        """
        self['set']('hour', hour)
        self['set']('minute', minute)

    def __str__(self):
        """
        Get the string representation of the time.
        :return: The string representation of the time in the format "hour:minute"
        """
        return f"'{self['get']('hour')}:{self['get']('minute'):02d}'"

    return make_class({'__init__': __init__, '__str__': __str__})


def make_calentry_class():
    """
    Create a new class for representing calendar entries.
    :return: A new class for representing calendar entries
    """
    def __init__(self, year, month, day):
        """
        Initialize a new calendar entry instance with the given year, month, and day.
        :param year: The year of the calendar entry
        :param month: The month of the calendar entry
        :param day: The day of the calendar entry
        """
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)
        self['set']('tasks', {})

    def addTask(self, task, start, end):
        """
        Add a task to the calendar entry
        :param task: The task to add
        :param start: The start time of the task
        :param end: The end time of the task
        """
        self['get']('tasks')[start['get']('__str__')(), end['get']('__str__')()] = task

    return make_class({'__init__': __init__, 'addTask': addTask})


Date = make_date_class()
today = Date['new'](2017, 1, 20)
print(today['get']('year'))
CalendarEntry = make_calentry_class()
todo = CalendarEntry['new'](2017, 1, 20)
Time = make_time_class()
t = Time['new'](10, 0)
print(t['get']('__str__')())
todo['get']('addTask')("PPL lecture", t, Time['new'](13, 0))
todo['get']('addTask')("PPL homework#4", Time['new'](14, 0), Time['new'](16, 0))
print(todo['get']('tasks'))
