import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if a == 0:
    print("This is not quadratic equation, plese enter the coefficients correctly")
else:
    discriminant = b * b - 4 * a * c
    square_root= math.sqrt(abs(discriminant))
    if discriminant> 0:
        print("The roots are real and different. The roots are: ")
        print((-b + square_root)/(2 * a))
        print((-b - square_root)/(2 * a))
    elif discriminant == 0:
        print("The roots are real and same. The roots are:")
        print(-b / (2 * a))
    else:
        print("The roots are complex and different. The roots are:")
        print(- b / (2 * a), " + i", square_root/(2*a))
        print(- b / (2 * a), " - i", square_root/(2*a))