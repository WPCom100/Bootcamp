# Type Casting Practice 
num = input("Type a two digit number: ")

print(num[0] + " + " +  num[1] + " = " + str(int(num[0]) + int(num[1])))


# Mathmatical Operators Practice
weight = float(input("Weight: "))
height = float(input("Height: "))

BMI = (weight) / (height ** 2)

print("BMI: " + str(int(BMI)))


# Using fStrings
age = int(input("Age: "))

yearsLeft = 90 - age
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12
daysLeft = yearsLeft * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks, or {monthsLeft} months left.")

