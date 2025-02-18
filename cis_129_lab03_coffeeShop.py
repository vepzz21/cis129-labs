'''
Emmanuel Piña-Zelinger
CIS129
Module 3: Lab
The purpose of this lab is to create an interactive text-based Coffee
Shop simulator that calculates a receipt based on how many items the 
user wants to order.
'''


def coffeeShop():
    '''
    This function obtains menu-input from cusstomer, calculates pricing
    based on input, and generates a receipt, containing the total of 
    what the customer purchased.
    Also, this function follows the IPO procedure. 
    '''
    #below is the input.
    coffee_request = int(input("Hi! Enter desired cups of coffee: "))
    coffee_order = str(coffee_request)
    muffin_request = int(input("Enter desired number of muffins: "))
    muffin_order = str(muffin_request)
    bagel_request = int(input("Enter desired number of bagels: "))
    bagel_order = str(bagel_request)
    breakfastBurrito_request = int(input("Enter desired number of burritos: "))
    breakfastBurrito_order = str(breakfastBurrito_request)

    #below is the processing.
    coffee_calculation = coffee_request * 5
    formatted_coffee_calculation = "{:.2f}".format(coffee_calculation)
    muffin_calculation = muffin_request * 4
    formatted_muffin_calculation = "{:.2f}".format(muffin_calculation)
    bagel_calculation = bagel_request *4.50
    formatted_bagel_calculation = "{:.2f}".format(bagel_calculation)
    breakfastBurrito_calculation = breakfastBurrito_request*7
    formatted_breakfastBurrito_calculation = "{:.2f}\
    ".format(breakfastBurrito_calculation)
    tax_calculation = float(((coffee_calculation + muffin_calculation/
    +bagel_calculation+breakfastBurrito_calculation)*0.06))
    tax = round(tax_calculation,2)
    total = float((coffee_calculation+muffin_calculation+tax\
    +bagel_calculation+breakfastBurrito_calculation))

    #below is the output. 
    receipt = "***************************************\
\nMy Coffee and Muffin Shop\
\nNumber of coffees bought?\
\n"+coffee_order+"\nNumber of muffins bought?\
\n"+muffin_order+"\nNumber of bagels bought?\n" +bagel_order+"\
\nNumber of burritos bought?\n"+breakfastBurrito_order+"\
\n***************************************\
\n\
\n***************************************\
\nMy Coffee and Muffin Shop Receipt"+"\n"+coffee_order+"\
 Coffee at $5 each: $"+str(formatted_coffee_calculation)+"\
\n"+bagel_order+" Muffins at $4 each: $"+formatted_muffin_calculation+"\
\n"+bagel_order+" Bagels at $4.50 each: $"+formatted_bagel_calculation+"\
\n"+breakfastBurrito_order+" Breakfast Burritos at $7 each: \
$"+formatted_breakfastBurrito_calculation+"\
\n6% tax: $"+str(tax)+"\
\n---------\
\nTotal: $"+str(total)+"\
\n***************************************\
\nThank you for your patronage."
    print(receipt)

coffeeShop()
