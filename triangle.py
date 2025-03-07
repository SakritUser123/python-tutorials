first = int(input('Enter the first side of the triangle'))
second = int(input("Enter the secod side of the triangle"))

third = int(input("Enter the third side of the triangle"))

if first == second and first == third:
    print('This is a equilateral triangle')
elif first == second and first != third or first == third and first != second:
    print("This is a isoceles triangle")
elif first != second and first != third:
    print("This is a scalene triangle")
