# Exercise 1
# temperature = float(input("What is your temperature today? "))
# if temperature < 35:
#     print("Not too cold")
# elif  temperature > 37:
#     print("Posible fever! Buddy, get yourself in bed with tea!")
# else:
#     print("All right!")

# #Exercise2

monthly_salary = float(input("What is your montly salary? "))
years_worked = float(input("How many years have you worked here? "))
bonus_rate = 0.15
bonus_treshold = 2
if years_worked < 2:
    print("Your bonus amount is 0! Don't be sad, your bonus is coming next year, keep up the good work!")
else:
    bonus = str(round((years_worked - bonus_treshold) * monthly_salary * bonus_rate))
    print("Your bonus comes up to " + bonus)