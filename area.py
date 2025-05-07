pi = 3.14
print("Area Calculator".center(100))

def area():
    unit = input("\nChoose the unit (centimeter/meter)? : ").lower()
    if unit == 'centimeter' or unit == 'meter':
        print("\n\t\tShapes Of The Area")
        print("1. Triangle")
        print("2. Circle")
        print("3. Square")
        print("4. Rectangle")
        user = int(input("\nChoose the shape : "))

        if user == 1:
            print("TRAINGLE".center(100))
            h = float(input("Height : "))
            base = float(input("Base : "))
            area = 0.5 * base * h
            print(f"Area = {area} {unit} sq")
        elif user == 2:
            print("CIRCLE".center(100))
            r = float(input("Radius of the Circle : "))
            areac = pi * r ** 2
            print(f"Area = {areac} {unit} sq")
        elif user == 3:
            print("SQUARE".center(100))
            s = float(input("Side of the Square : "))
            area = s ** 2
            print(f"Area = {area} {unit} sq")
        elif user == 4:
            print("RECTANGLE".center(100))
            l = float(input("Length : "))
            b = float(input("Breadth : "))
            area = l * b
            print(f"Area = {area} {unit} sq")
        else:
            print("Invalid Input")
    else:
        print("Please enter valid unit")

while True:
    area()
    ask = input("\nDo you want to perform another calculation? (yes/no): ")
    if ask.lower() != 'yes':
        break

print("Thank you for using the Area Calculator!")
