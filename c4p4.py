print("Name : Antony raju\nRoll No : 15")

class Time:
    def __init__(self):
        while True:
            try:
                self.__h = int(input("Enter the hour (0-23): "))
                if self.__h < 0 or self.__h >= 24:
                    raise ValueError("Hour must be between 0 and 23.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.__m = int(input("Enter the minute (0-59): "))
                if self.__m < 0 or self.__m >= 60:
                    raise ValueError("Minute must be between 0 and 59.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.__s = int(input("Enter the second (0-59): "))
                if self.__s < 0 or self.__s >= 60:
                    raise ValueError("Second must be between 0 and 59.")
                break
            except ValueError as e:
                print(e)

    def __add__(self, time2):
        hour = self.__h + time2.__h
        minute = self.__m + time2.__m
        second = self.__s + time2.__s

        if second >= 60:
            minute += second // 60
            second = second % 60

        if minute >= 60:
            hour += minute // 60
            minute = minute % 60

        if hour >= 24:
            hour = hour % 24

        print("Sum of Hours:", hour)
        print("Sum of Minutes:", minute)
        print("Sum of Seconds:", second)

print("Time of first object")
time1 = Time()
print("Time of second object")
time2 = Time()

print("-------------------")
time1.__add__(time2)
print("-------------------")

