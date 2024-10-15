# Open the file in read mode to check for existing usernames and passwords
file = open("ID.txt", "r")
data = file.read()  # Read the content of the file
print(data)
file.close()  # Close the file after reading

ok = False  # Variable to indicate if the process is completed successfully

# Ask the user for their username
username = input("write username:  ")
if username in data:  # Check if the username exists in the file
    pasword = input("write pasword: ")  # Ask for the password if the username is found
    if pasword in data:  # Check if the password is correct
        print("You are logged in")
    else:
        next  # Placeholder to continue if the password is incorrect

# If the password is not correct, allow the user to set a new username and password
if pasword not in data:
    print("wrong password!")
    next
    username = input("please, write your new username: ")
    while not ok:  # Loop until a valid username is provided
        if username in data:  # If the username already exists, ask again
            continue
        else: 
            if len(username) <= 6:  # Ensure the username is longer than 6 characters
                print("Your username is too short!")
                continue
            # Loop to ensure the password is valid
            while not ok:
                pasword = input("write password: ")
                if pasword not in username:  # Ensure password is not part of the username
                    print("Wrong password!")
                    pasword = input("Please, write your new password: ")
                    pasword1 = input("Please, write again your new password: ")
                    while not ok:  # Loop to confirm the new password
                        if pasword in data:  # Ensure the password is not already in use
                            continue
                        else:
                            if pasword != pasword1:  # Check if both passwords match
                                print("The passwords do not match!")
                                continue
                            else:
                                if len(pasword and pasword1) <= 6:  # Ensure password length is sufficient
                                    print("Your new password is too short!")
                                else:
                                    # If everything is fine, set the flag to True and save the new user
                                    ok = True
                                    file = open("ID.txt", "a")  # Open the file in append mode
                                    file.write("\n" + username + "," + pasword1)  # Add the new username and password
                                    file.close()  # Close the file after writing
                                    print("You have successfully logged in. :)")
