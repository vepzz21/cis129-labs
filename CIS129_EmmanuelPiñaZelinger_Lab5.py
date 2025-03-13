'''
Emmanuel Piña-Zelinger 
03/12/2025
This program allows a grocery store to keep track of the total number of
bottles collected for seven days. 
'''


def main():
    # Step 1: Declare variables
    keepGoing = "y"  # Variable used to determine if the program runs again

    # Step 2: Program logic
    while keepGoing.lower() == "y":
        # Get the total bottles returned for the week
        total_bottles = get_bottles()

        # Calculate the payout based on the total bottles
        total_payout = calc_payout(total_bottles)

        # Print the total bottles and total payout
        print_info(total_bottles, total_payout)

        # Step 3: Ask the user if they want to enter data for another week
        keepGoing = input("\nDo you want to enter another week's worth of data? (Enter y or n): ")

def get_bottles():
    """Function to get the number of bottles returned for each day."""
    total_bottles = 0
    for day in range(1, 8):  # Loop over 7 days
        while True:
            today_bottles = int(input(f"Enter the number of bottles returned on day {day}: "))
            total_bottles += today_bottles  # Add the entered bottles to the total
            break  # Exit the loop if input is valid
    return total_bottles


def calc_payout(total_bottles):
    """Function to calculate the payout based on the total bottles."""
    total_payout = total_bottles * 0.10  # Each bottle is worth 10 cents
    return total_payout


def print_info(total_bottles, total_payout):
    """Function to display the results of the total bottles and payout."""
    print(f"\nTotal bottles returned for the week: {total_bottles}")
    print(f"Total paid out: ${total_payout:.2f}")

main()
