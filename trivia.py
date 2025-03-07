print("Geography Trivia!")
score = 0
geo = int(input('How many countries are there in the world officialy in the UN'))
if geo == 193:
    score += 1
    print("You got the answer correct + 1 points")
nex = input('What country has the highest mountain that is above land? ')
if nex.lower() == "nepal":
    score += 1
    print("You got the answer correct +1 points")

ast = input("What is the largest landlocked country in the world ")
if ast.lower() == "mongolia":
    score += 1
    print("You have got this answer correct +1 ")


ws = input("What country has the smallest population in the world other than vatican city?")
if ws.lower() == "niue":
    score += 1
    print("You have got this answe correct")
print('Bonus Question!!!!!')




