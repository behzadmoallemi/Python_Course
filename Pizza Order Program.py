print("Welcome to the PRIMA Pizza Deliveries!")
size = input("What size pizza would you like to order? \nPlease type S for Small, M for Medium and L for Large\nSize: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry! Your input is invalid! \nPlease start again and use S, M or L for your pizza size.")
    exit()

pepp = input("Would you like extra Pepperoni on your Pizza? \nPlease type Y for Yes and N for No\nExtra Pepperoni: ")
if size == "S" and pepp == "Y":
    bill += 2
elif size == "M" and pepp == "Y" or size == "L" and pepp == "Y":
    bill+= 3
elif pepp == "N":
    bill = bill
else:
    print("Sorry! Your input for extra pepperoni is invalid! \nPlease start again and use Y or N.")
    exit()
cheese = input("Would you like extra cheese on your Pizza? \nPlease type Y for Yes and N for No\nExtra Cheese: ")
if cheese == "Y":
    bill += 1
elif cheese == "N":
    bill = bill
else:
    print("Sorry! Your input for extra cheese is invalid! \nPlease start again and use Y or N.")
    exit()
print(f"Your final bill is: ${bill}")