class InvalidDateError(Exception):
    """
    Exception raised when an invalid value is provided for a date.
    """
    def __init__(self, value):
        """
        Initialize the exception with the invalid value.
        :param value: The invalid value provided for the date
        """
        self.value = value

    def __str__(self):
        """
        Get the string representation of the exception.
        :return: The string representation of the exception in the format "Invalid value for date: value"
        """
        return f"Invalid value for date: {self.value}"


class InvalidTimeError(Exception):
    """
    Exception raised when an invalid value is provided for a time.
    """
    def __init__(self, value):
        """
        Initialize the exception with the invalid value.
        :param value: The invalid value provided for the time
        """
        self.value = value

    def __str__(self):
        """
        Get the string representation of the exception.
        :return: The string representation of the exception in the format "Invalid value for time: value"
        """
        return f"Invalid value for time: {self.value}"


class TaskOverlapTimeError(Exception):
    """
    Exception raised when a task's time is overlapping with the time of an existing task.
    """
    def __init__(self, value):
        """
        Initialize the exception with the given value.
        :param value: The value that caused the exception
        """
        self.value = value

    def __str__(self):
        """
        Get a string representation of the exception.
        :return: A string representation of the exception
        """
        return f"The time of this task: {self.value}, is overlapping with the time of an existing task."


class Date:
    """
    This class represents a date, with a year, month, and day.
    """
    def __init__(self, year, month, day):
        """
        Initialize a new date object with the given year, month, and day.
        :param year: The year of the date (4-digit integer)
        :param month: The month of the date (1-12)
        :param day: The day of the date (1-31)
        :raises InvalidDateError: If the year, month, or day is invalid
        """
        while True:
            try:
                if 999 > year or year > 9999:
                    raise InvalidDateError(year)
                if month < 1 or month > 12:
                    raise InvalidDateError(month)
                if day < 1 or day > 31:
                    raise InvalidDateError(day)
                self.year = year
                self.month = month
                self.day = day
                break
            except InvalidDateError as e:
                if e.value == year:
                    print(type(e).__name__+':', e)
                    year = int(input("Enter valid year: "))
                elif e.value == month:
                    print(type(e).__name__ + ':', e)
                    month = int(input("Enter valid month: "))
                else:
                    print(type(e).__name__ + ':', e)
                    day = int(input("Enter valid day: "))

    def __str__(self):
        """
        Return a string representation of the date in the format "dayst/nd/rd/th of month, year"
        :return: A string representation of the date
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
        Return a string representation of the date in the format "Date(year, month, day)"
        :return: A string representation of the date
        """
        return f"Date({self.year}, {self.month}, {self.day})"


class Time:
    """
    This class represents a time, with an hour and a minute.
    """
    def __init__(self, hour, minute):
        """
        Initializes a Time object with the given hour and minute.
        If the hour or minute is invalid, raises an InvalidTimeError.
        :param hour: Integer representing the hour, between 0 and 23.
        :param minute: Integer representing the minute, between 0 and 59.
        """
        while True:
            try:
                if hour > 23 or hour < 0:
                    raise InvalidTimeError(hour)
                if minute > 59 or minute < 0:
                    raise InvalidTimeError(minute)
                self.hour = hour
                self.minute = minute
                break
            except InvalidTimeError as t:
                if t.value == hour:
                    print(type(t).__name__ + ':', t)
                    hour = int(input("Enter valid hour: "))
                else:
                    print(type(t).__name__ + ':', t)
                    minute = int(input("Enter valid minute: "))

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

    def overlap_time(self, start, end):
        """
        This method check if there is an overlap in time between the given start and end times and the tasks stored in the `tasks` attribute of the class instance.
        :param start: starting time of the task as a string
        :param end: ending time of the task as a string
        :return: True if there is an overlap in time and False otherwise.
        """
        start_time = str(start)
        end_time = str(end)
        for task_start, task_end in self.tasks:
            if (task_start <= start_time < task_end) or (task_start < end_time <= task_end):
                return True
        return False

    def addTask(self, task, start, end):
        """
        Adds a task to the CalendarEntry's list of tasks.
        :param task: String representing the task to be added.
        :param start: Time object representing the start time of the task.
        :param end: Time object representing the end time of the task.
        """
        try:
            if self.overlap_time(start, end):
                raise TaskOverlapTimeError(f"{start} - {end}")
            start_time = str(start)
            end_time = str(end)
            self.tasks[(start_time, end_time)] = task
        except TaskOverlapTimeError as e:
            print(e)
            new_start = input("Enter new start time: ")
            new_end = input("Enter new end time: ")
            self.addTask(task, new_start, new_end)

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
         format "To do list for date: task1: start_time-end_time, task2: start_time-end_time".
        :return: string representation of the CalendarEntry object.
        """
        convert_task = "Todo list for " + str(self.date) + ":\n"
        for i, (times, task) in enumerate(sorted(self.tasks.items())):
            convert_task += f"{i + 1}. {times[0]}-{times[1]} - {task}\n"
        return convert_task


month_name = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November",
              12: "December"}

today = Date(22, 13, 20)
print(repr(today))
print(today.year)
print(today)
todo = CalendarEntry(2017, 1, 20)
t = Time(10, 0)
print(str(t))
todo.addTask("PPL lecture", t, Time(13, 0))
todo.addTask("PPL homework#4", Time(11, 0), Time(16, 0))
print(todo.tasks)
print(todo)
