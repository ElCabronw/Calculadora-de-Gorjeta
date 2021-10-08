print("Welcolme to the tip calculator \n")
totalBill = input("What as the total bill? $")
new_bill = float(totalBill)

percentage = input("\What percentage tip would you like to give?10,12 or 15?")
peopleQuantity = input("How many people to split the bill?")

total = (float(totalBill)/int(peopleQuantity)) * (1+(int(percentage)/100))
print(f"Each person should pay: ${round(total,2)}")