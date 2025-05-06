pi = 3.14
print("\t\tArea Calculator")

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
            print("\t\tTRAINGLE")
            h = float(input("Height : "))
            base = float(input("Base : "))
            area = 0.5 * base * h
            print(f"Area = {area} sq {unit}")
        elif user == 2:
            print("\t\tCIRCLE")
            r = float(input("Radius of the Circle : "))
            areac = pi * r ** 2
            print(f"Area = {areac} sq {unit}")
        elif user == 3:
            print("\t\tSQUARE")
            s = float(input("Side of the Square : "))
            area = s ** 2
            print(f"Area = {area} sq {unit}")
        elif user == 4:
            print("\t\tRECTANGLE")
            l = float(input("Length : "))
            b = float(input("Breadth : "))
            area = l * b
            print(f"Area = {area} sq {unit}")
        else:
            print("Invalid Input")
    else:
        print("Please enter valid unit")

while True:
    area()
    ask = input("Do you want to perform another calculation? (yes/no): ")
    if ask.lower() != 'yes':
        break

print("Thank you for using the Area Calculator!")
