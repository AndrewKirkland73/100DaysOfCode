import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_list = list(names)
bill_payer = random.choice(names_list)

print(f"{bill_payer}, will buy this meal!")