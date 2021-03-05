#Odd and Even Checker
# number = int(input("What number do you want me to check? "))

# if (number % 2) == 1:
#     print(f"{number} is and odd number!")
# elif number == 0:
#     print(f"Invalid number {number}")
# else:
#     print(f"{number} is and even number!")


# If, else, and elif Practice
# weight = float(input("Weight: "))
# height = float(input("Height: "))

# BMI = (weight) / (height ** 2)

# print(f"BMI: {round(BMI)}")

# if BMI < 18.5:
#     print("You are underweight")
# elif (BMI >= 18.5) & (BMI < 25):
#     print("You are normal")
# elif (BMI >= 25) & (BMI < 30):
#     print("You are slightly over")
# elif (BMI >= 30) & (BMI < 35):
#     print("You are obtuse")
# else:
#     print("You are clenicly obtuse")


# Leap year calculator
# year = int(input("What is the year you would like to check? "))

# if year % 4 == 0 & year % 100 != 0:
#     print(f"{year} is a leap year!")
# elif year % 400 == 0:
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year!")

# Pizza Ordering Exercise
pizzaSize = input("What size Pizza? s/m/l ")
pizzaPepperoni = input("Do you want pepperoni? y/n ")
pizzaCheese = input("Do you want extra cheese? y/n ")

totalCost = int()

if pizzaSize == "s" or pizzaSize == "S":
    totalCost += 15
    if pizzaPepperoni == "y" or pizzaPepperoni == "Y":
        totalCost += 2
elif pizzaSize == "m" or pizzaSize == "M":
    totalCost += 20
    if pizzaPepperoni == "y" or pizzaPepperoni == "Y":
        totalCost += 3
elif pizzaSize == "l" or pizzaSize == "L":
    totalCost += 25
    if pizzaPepperoni == "y" or pizzaPepperoni == "Y":
        totalCost += 3

if pizzaCheese == "y" or pizzaCheese == "Y":
    totalCost += 1

print(f"Your total cost will be: {totalCost}")
