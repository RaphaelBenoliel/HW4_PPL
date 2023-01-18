

class InvalidDateError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Invalid value for date: {self.value}"


class InvalidTimeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Invalid value for time: {self.value}"


class TaskOverlapTimeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"The time of this task: {self.value}, is overlapping with the time of an existing task."


class Date:
    def __init__(self, year, month, day):
        """
        :param year:
        :param month:
        :param day:
        """
        while True:
            try:
                if year < 1:
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
                    print(e)
                    year = int(input("Enter valid year: "))
                elif e.value == month:
                    print(e)
                    month = int(input("Enter valid month: "))
                else:
                    print(e)
                    day = int(input("Enter valid day: "))

    def __str__(self):
        if self.day in (1, 21, 31):
            return f"'{self.day}st of {month_name[self.month]}, {self.year}'"
        elif self.day in (2, 22):
            return f"'{self.day}nd of {month_name[self.month]}, {self.year}'"
        elif self.day in (3, 23):
            return f"'{self.day}rd of {month_name[self.month]}, {self.year}'"
        else:
            return f"'{self.day}th of {month_name[self.month]}, {self.year}'"

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"


class Time:
    def __init__(self, hour, minute):
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
                    print(t)
                    hour = int(input("Enter valid hour: "))
                else:
                    print(t)
                    minute = int(input("Enter valid minute: "))

    def __str__(self):
        return f"{self.hour}:{self.minute:02d}"

    def __repr__(self):
        return f"Time({self.hour}, {self.minute})"


class CalendarEntry:
    def __init__(self, year, month, day):
        self.date = Date(year, month, day)
        self.tasks = {}

    def overlap_time(self, start, end):
        start_time = str(start)
        end_time = str(end)
        for task_start, task_end in self.tasks:
            if (task_start <= start_time < task_end) or (task_start < end_time <= task_end):
                return True
        return False

    def addTask(self, task, start, end):
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
        return f"CalendarEntry({self.date})"

    def __str__(self):
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
todo.addTask("PPL homework#4", Time(11, 0), Time(16, 0))
print(todo.tasks)
print(todo)
