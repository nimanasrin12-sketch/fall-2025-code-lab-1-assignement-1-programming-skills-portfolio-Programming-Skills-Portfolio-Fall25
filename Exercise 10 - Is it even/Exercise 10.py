def check_even_odd(number):
    # This function checks if the number is even or odd
    if number % 2==0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    # Ask user for a number
    num = int(input("Enter a number: "))

    # Call the function and store the message
    message = check_even_odd(num)

    # Print the message
    print(message)

if __name__ == "__main__":
    main()