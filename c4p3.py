print("Name : Antony raju\nRoll No : 15")

class Rectangle:
    def __init__(self):
        while True:
            try:
                self.__length = int(input("Enter the length: "))
                if self.__length <= 0:
                    raise ValueError("Length must be a positive integer.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.__breadth = int(input("Enter the breadth: "))
                if self.__breadth <= 0:
                    raise ValueError("Breadth must be a positive integer.")
                break
            except ValueError as e:
                print(e)

    def __lt__(self, ob2):
        area1 = self.__length * self.__breadth
        area2 = ob2.__length * ob2.__breadth
        print("Area of Rectangle 1:", area1)
        print("Area of Rectangle 2:", area2)
        return area1 < area2

print("Rectangle 1")
obj1 = Rectangle()

print("Rectangle 2")
obj2 = Rectangle()

print("-------------------------")
if obj1 < obj2:
    print("Rectangle 1 is smaller.")
else:
    print("Rectangle 2 is smaller.")
