#Tip Calculator
print("Welcome to the tip calculator!")

totalBill = float(input("What was the bill total? "))

tipPercentage = (float(input("What is the % tip you would like to give? ")) * .01) + 1
peopleSplit = int(input("The number of people splitting the bill? "))

result = (totalBill * tipPercentage) / peopleSplit

print(f"Each person should pay: {'{:.2f}'.format(round(result, 2))}")
 
