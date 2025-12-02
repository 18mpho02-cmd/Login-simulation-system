def login_system():
	# Step 1: Declare the correct username and password
    correct_username = "mphozane"
    correct_password = "31314"

    # Step 2: Give the user 3 attempts to log in
    attempts = 3

    # Step 3: Loop until the user runs out of attempts
    while attempts > 0: 
        print("\nLogin System")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Step 4: Check if username and password are correct
        if username == correct_username and password == correct_password:
            print("Login successful! Welcome,", username)
            break # stop the loop
        else:
            attempts -= 1
            print("Incorrect username or password.")
            print(" Attempts remaining:", attempts)

    # Step 5: If no attempts left, lock the user out
            if attempts == 0:
                print("You have been locked out due to too many failed login attempts.")

# Run the program
login_system()