

def make_class(attributes, base_class=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
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
    attributes = {}

    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value


def make_date_class():
    def __init__(self, year, month, day):
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)

    return make_class({'__init__': __init__})


def make_time_class():
    def __init__(self, hour, minute):
        self['set']('hour', hour)
        self['set']('minute', minute)

    def __str__(self):
        return f"'{self['get']('hour')}:{self['get']('minute'):02d}'"

    return make_class({'__init__': __init__, '__str__': __str__})


def make_calentry_class():
    def __init__(self, year, month, day):
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)
        self['set']('tasks', {})

    def addTask(self, task, start, end):
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
