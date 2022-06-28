import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']
combined_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
password = []
print(combined_letters)


print("Welcome to the Pypassword Generator!")
nr_letters = int(input("How many letters would you like in your passowrd? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

for x in range(nr_letters):
    password.append(random.choice(combined_letters))

for x in range(nr_symbols):
    password.append(random.choice(symbols))

for x in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print("".join(password))
