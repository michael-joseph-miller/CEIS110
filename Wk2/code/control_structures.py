bonus = 30
if bonus < 10:
    bonus = 100
else:
    bonus = 200
print("\nbonus =", bonus, "\n")

age = int(input("Enter your age: "))
if age < 18:
    print("You cant vote or drink.")
elif age >= 18 and age < 21:
    print("You can vote but you can't drink")
elif age >= 21 and age < 65:
    print("I dont know")
elif age >= 65:
    print("You can retire.")
elif not age < 70:
    print("Your over 70")
else:
    print("You can vote and drink")
