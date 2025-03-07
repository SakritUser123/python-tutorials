x = int(input("Enter a X Coordinate: "))

y = int(input("Enter a Y coordinate: "))


if x > 0 and y > 0:
    print("Your coordinate is in first quadrant")
elif x > 0 and y < 0:
    print("Your coordinate is in quadrant 4")
elif x < 0 and y > 0:
    print("Your coordinate is in quadrant 2")
elif x < 0 and y <0:
    print("Your coordinate is in third quadrant")
elif y == 0 and x ==0:
    print("Your coordinate is the origin")
else:
    print("Your coordinate is on a axis")
        
