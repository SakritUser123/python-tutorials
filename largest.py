first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
third = int(input("Enter your third number: "))


if first > second and first > third:
    first = str(first)
    print("The largest number is " + first)
    
elif second > first and second > third:
    second = str(second)
    print("The largest number is " + second)
    
elif third > first and third >second:
    third = str(third)
    print('The largest number is ' + third)
else:
    print("all numbers are equal")
