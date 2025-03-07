month = int(input("Enter The month"))

day = int(input("Enter The month"))

year = int(input('Enter the year'))

if year < 1800 or year > 2100:
    print(month , '/' , day , '/' , year)
    print("Date range is 1800 - 2100")

if day > 31 :
    print(month , '/' , day , '/' , year)
    print("Invalid Day number")


if month > 12:
    print(month , '/' , day , '/' , year)
    print("Invalid month")

leap = False

if year % 4 == 0:
    print(month , '/' , day , '/' , year)
    print("This is leap year")
    leap = True
if leap == False and month == 2 and day > 29:
    print(month , '/' , day , '/' , year)
    print("Date invalid as it is a leap year")

if month == 4 or month == 6 or month == 9 or month == 11 and days >30:
    print(month , '/' , day , '/' , year)
    print("Invalid number of days for that month")
if month == 1 or month == 3 or month == 7 or month == 8 or month == 10 or month == 12 and days > 31:
   print(month , '/' , day , '/' , year)
   print("Invalid number of days") 
