# A dictionary containing usernames as keys and passwords as values
ID = {"martin": 1234568, "adam": 1234}

# Print the current dictionary of IDs
print(ID)

# Define variable types for username and password
username = str
pasword = int

# Access the keys and values from the dictionary
username = ID.keys
pasword = ID.values

# Prompt the user to input their username
username = input("Enter your username: ")  # "Login username"
if username in ID:  # Check if the username exists in the ID dictionary
    print("Correct username")  # "Correct username"
else:
    print("Wrong username")  # "Wrong username"

# Prompt the user to input their password
pasword = input("Enter your Password: ")  # "Password"
if pasword not in username:  # Check if the password is correct for the username
    print("You entered the wrong password")  # "You entered the wrong password"
else:
    print("Logging in")  # "Logging in"

# Define a function to validate passwords
def pasword():
    for pasword in ID.values():  # Loop through the password values in the dictionary
        if pasword == False:  # If the password is False (invalid)
            if username == False:  # Check if the username is also invalid
                return username  # Return the username
