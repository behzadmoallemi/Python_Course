import random
letters = ['b', 'f', 'v', 'q', 's', 'w', 'y', 'l', 'g', 'j', 'z', 'c', 'h', 'p', 'x', 'd', 'm', 'n', 't', 'k', 'r']
numbers = [ "1", "2", "3", "4", "5"]
symbols = ["@", "#", "$", "%", "&"]

letters_num = int(input("How many letters do you want your password to have?"))
numbers_num = int(input("How many numbers do you want your password to have?"))
symbols_num = int(input("How many symbols do you want your password to have?"))

password_list = []

for char in range(1, letters_num +1):
    password_list += random.choice(letters)

for char in range(1, numbers_num +1):
    password_list += random.choice(numbers)

for char in range(1, symbols_num +1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(password)