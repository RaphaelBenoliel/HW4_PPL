
class Date:
    """
    This class represents a date, with a year, month, and day.
    """
    def __init__(self, year, month, day):
        """
        Initialize a new Date object with the specified year, month, and day.
        :param year: an integer representing the year, in YYYY format.
        :param month: an integer representing the month, between 1 and 12.
        :param day: an integer representing the day, between 1 and the number of days in the given month.
        """
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        """
        Return a string representation of the date in the format "day(st/nd/rd/th) of month, year".
        """
        if self.day in (1, 21, 31):
            return f"'{self.day}st of {month_name[self.month]}, {self.year}'"
        elif self.day in (2, 22):
            return f"'{self.day}nd of {month_name[self.month]}, {self.year}'"
        elif self.day in (3, 23):
            return f"'{self.day}rd of {month_name[self.month]}, {self.year}'"
        else:
            return f"'{self.day}th of {month_name[self.month]}, {self.year}'"

    def __repr__(self):
        """
        Return a string representation of the date in the format "Date(year, month, day)".
        """
        return f"Date({self.year}, {self.month}, {self.day})"


class Time:
    """
    This class represents a time, with an hour and a minute.
    """
    def __init__(self, hour, minute):
        """
        Initializes a Time object with the given hour and minute.
        :param hour: Integer representing the hour, between 0 and 23.
        :param minute: Integer representing the minute, between 0 and 59.
        """
        self.hour = hour
        self.minute = minute

    def __str__(self):
        """
        Returns a string representation of the Time object in the format "HH:MM".
        :return: String representation of the Time object.
        """
        return f"{self.hour}:{self.minute:02d}"

    def __repr__(self):
        """
        representation of the Time object that can be used to recreate the object using the Time() constructor.
        :return: String representation of the Time object.
        """
        return f"Time({self.hour}, {self.minute})"


class CalendarEntry:
    """
    This class represents an entry in a calendar, with a date and a list
    """
    def __init__(self, year, month, day):
        self.date = Date(year, month, day)
        self.tasks = {}

    def addTask(self, task, start, end):
        """
        Adds a task to the CalendarEntry's list of tasks.
        :param task: String representing the task to be added.
        :param start: Time object representing the start time of the task.
        :param end: Time object representing the end time of the task.
        """
        start_time = str(start)
        end_time = str(end)
        self.tasks[(start_time, end_time)] = task

    def __repr__(self):
        """
        representation of the CalendarEntry object that can be used to recreate the object using the CalendarEntry()
        constructor.
        :return: String representation of the CalendarEntry object.
        """
        return f"CalendarEntry({self.date})"

    def __str__(self):
        """
        Returns a string representation of the CalendarEntry object that lists the tasks scheduled for the date in the
        format "to do list for date: task1: start_time-end_time, task2: start_time-end_time".
        :return: string representation of the CalendarEntry object.
        """
        convert_task = "Todo list for " + str(self.date) + ":\n"
        for i, (times, task) in enumerate(sorted(self.tasks.items())):
            convert_task += f"{i + 1}. {times[0]}-{times[1]} - {task}\n"
        return convert_task


month_name = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November",
              12: "December"}

today = Date(2017, 1, 20)
print(repr(today))
print(today.year)
print(today)
todo = CalendarEntry(2017, 1, 20)
t = Time(10, 0)
print(str(t))
todo.addTask("PPL lecture", t, Time(13, 0))
todo.addTask("PPL homework#4", Time(14, 0), Time(16, 0))
print(todo.tasks)
print(todo)
