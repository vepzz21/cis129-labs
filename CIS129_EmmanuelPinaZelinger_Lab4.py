'''
Module 4 Lab
Emmanuel Piña-Zelinger
CIS 129
02/25/2025
This program modifies the retail company's bonus portion to include 
different levels and types and eliminates the day-off program.
'''


def main():
    #declare local variables
    monthlySales = 0
    storeAmount = 0
    empAmount = 0
    salesIncrease = 0

def getSales(prompt):
    #This function gets the monthly sales
    monthlySales = float(input(prompt))
    return monthlySales

def calcStoreBonus(monthlySales):
    #This function determines the storeAmount bonus 
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

def getIncrease(prompt):
    #This function gets the percent of increase in sales
    salesIncrease = float(input("Enter the percent of sales increase in decimal format: "))
    salesIncrease = salesIncrease/100
    return salesIncrease

def calcEmpBonus(salesIncrease):
    #This function determines the empAmount bonus
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

def printBonus(storeAmount, empAmount):
    #This function prints the bonus information
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print("Congrats! You have reached the highest bonus amounts possible! ")


main()