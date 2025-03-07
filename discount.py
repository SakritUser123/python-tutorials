aumont = int(input("Enter the total purchase aumont: "))

if aumont >= 100 :
    discount = 0.10 * aumont
    aumont = aumont-discount


elif aumont >= 50 and aumont <= 99:
    discount = 0.05 * aumont
    aumont = aumont - discount
else:
    disocunt = 0

aumont = str(aumont)
print("Your discounted price is: " + aumont)
    
