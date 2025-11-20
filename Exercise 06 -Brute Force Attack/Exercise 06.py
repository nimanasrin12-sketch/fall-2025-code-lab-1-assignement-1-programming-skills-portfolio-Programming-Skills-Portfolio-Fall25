# Exercise 06 - Brute Force Attack (Optional Version with 5 Attempts)

correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Maximum attempts reached! Authorities have been alerted")
            