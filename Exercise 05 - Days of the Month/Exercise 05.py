# Exercise 05 - Days of the Month (Advanced Version)

# Create a dictionary with month numbers and their corresponding days
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

# Ask the user to enter a month number
month = int(input("Enter the month number (1-12): "))

# Check if the input is valid
if 1 <= month <= 12:
    # If February, check for leap year
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            days_in_month[2] = 29

    # Display the number of days
    print(f"Number of days in month {month}: {days_in_month[month]}")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")