# Brayan Penaherrera, 03/31/2026, BrayanPenaherrera_PE4_1.py
# This program calculates a person's pay starting at 1 penny and doubling each day for the number of days entered.
# It shows each day's pay in dollars, the total pay and lets the user run the program again.

run_again = "1"

while run_again == "1":
    # Input
    days = int(input("Enter the number of days to work: "))

    # Initialize variables
    day = 1
    pennies = 1
    total_pennies = 0

    # Output headings
    print()
    print(" Day  Pay")
    print("---------------")

    # Loop through each day
    while day <= days:
        pay_in_dollars = pennies / 100
        print(day, "   $", format(pay_in_dollars, ",.2f"), sep="")
        total_pennies += pennies
        pennies *= 2
        day += 1

    # Display total salary
    total_salary = total_pennies / 100
    print()
    print("The total salary for", days, "days is: $",
          format(total_salary, ",.2f"), sep="")

    # Ask user if they want to run again the program
    run_again = input("1 = run again or press ENTER to end program ")

print()
print("Thanks for using our penny for pay program!")
