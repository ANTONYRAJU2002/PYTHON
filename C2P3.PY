def factors(n):
    factor = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor.append(i)
    return factor

area_square = lambda side: side ** 2
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height

while True:
    print("\nMenu:")
    print("1. Generate all factors of a number")
    print("2. Find area of square using lambda function")
    print("3. Find area of rectangle using lambda function")
    print("4. Find area of triangle using lambda function")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Factors of ",num,": ",factors(num))

    elif choice == 2:
        side = float(input("Enter the side of the square: "))
        print("Area of square:" ,area_square(side))

    elif choice == 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area of rectangle: ",area_rectangle(length, width))

    elif choice == 4:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("Area of triangle: ",area_triangle(base, height))

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")