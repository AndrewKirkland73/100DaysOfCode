def tipCalculator():

    print("Welcome to the tip calculator.")

    bill_amount = float(input("What is the total bill?"))
    tip_percent = int(input("What percent tip would you like to give?"))
    num_people = int(input("How many people to split the bill?"))
    tip_conversion = tip_percent / 100
    new_bill_amount = (tip_conversion * bill_amount)+bill_amount
    what_is_owed = round(new_bill_amount / num_people,2)
    print("Each person should pay: " + str(what_is_owed))

tipcalculator()