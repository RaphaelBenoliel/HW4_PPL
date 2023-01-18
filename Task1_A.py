

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

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
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour}:{self.minute:02d}"

    def __repr__(self):
        return f"Time({self.hour}, {self.minute})"


class CalendarEntry:
    def __init__(self, year, month, day):
        self.date = Date(year, month, day)
        self.tasks = {}

    def addTask(self, task, start, end):
        start_time = str(start)
        end_time = str(end)
        self.tasks[(start_time, end_time)] = task

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
todo.addTask("PPL homework#4", Time(14, 0), Time(16, 0))
print(todo.tasks)
print(todo)