print("Antony Raju \nRollnumber:15")

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def compare(self, other):
        if self.area() > other.area():
            print("1st rectangle has a greater area.")
        elif self.area() < other.area():
            print("2nd rectangle has a greater area.")
        else:
            print("Both rectangles have equal areas.")

try:
    length1 = int(input("Enter length of 1st rectangle: "))
    breadth1 = int(input("Enter breadth of 1st rectangle: "))
    obj1 = Rectangle(length1, breadth1)

    length2 = int(input("Enter length of 2nd rectangle: "))
    breadth2 = int(input("Enter breadth of 2nd rectangle: "))
    obj2 = Rectangle(length2, breadth2)

    print(f"1st rectangle -> Area: {obj1.area()} Perimeter: {obj1.perimeter()}")
    print(f"2nd rectangle -> Area: {obj2.area()} Perimeter: {obj2.perimeter()}")
    obj1.compare(obj2)

except ValueError:
    print("Invalid input! Please enter valid integer values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("Program executed successfully.")

finally:
    print("finally is executed")



