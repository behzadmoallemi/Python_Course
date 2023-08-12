names_string = input("Give me everybody's name, seperated by a comma. \n")
names = names_string.split(", ")
people = len(names)
import random
num = random.randint(0, people-1)
person = names[num]
print(f"{person} is going to buy the meal today!")