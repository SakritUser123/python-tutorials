age = int(input('Enter Your age: '))
money = 0
if age <= 12:
    money += 5
elif age >= 13 and age <= 17:
    money += 8
elif age >= 18 and age <= 59:
    money += 12
elif age >= 60:
    money += 7
else:
    print("You cannot watch the movie")
money = str(money)
print("The cost of the ticket is " + money + '$')
