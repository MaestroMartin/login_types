import json

# Open the JSON file and load the data into an object
with open("ID.json", "r") as file:
    data = file.read()  # Read the content of the file
    objekt = json.loads(data)  # Parse the JSON content into a Python object
    print(objekt)  # Print the object to see its structure

# A flag to indicate successful registration or login
ok = False

# Prompt the user to input their username
username = input("Enter your Username: ")  # "Login username"
if username in data:  # Check if the username exists in the loaded data
    pasword = input("Enter your Password: ")  # "Enter password"
    if pasword in data:  # Check if the password is correct
        print("You are logged in")  # "You are logged in"
    else:
        next  # Placeholder for continuing if the password is incorrect

# If the username is not found in the data
if username not in data:
    print("You entered the wrong Username!")  # "You entered the wrong username"
    next
    username = input("Enter your new Username:")  # "Enter a new username"
    while not ok:
        if username in data:  # Check if the username already exists
            continue
        else: 
            if len(username) <= 6:  # Check if the username is too short
                print("Yóur Username is too short !")  # "Your username is too short"
                continue
            # Prompt the user to enter a password
            while not ok:
                pasword = input("Enter your Password: ")  # "Password"
                if pasword not in username:  # Check if the password is not part of the username
                    print("You are entered wrong Password!")  # "You entered the wrong password"
                    pasword = input("Enter your new Password: ")  # "Enter new password"
                    pasword1 = input("Again enter your new Password: ")  # "Re-enter new password"
                    while not ok:
                        if pasword in data:  # Check if the password already exists
                            continue
                        else:
                            if pasword != pasword1:  # Ensure both passwords match
                                print("Passwords do not match!")  # "Passwords do not match"
                                break
                            else:
                                if len(pasword and pasword1) <= 6:  # Ensure password is not too short
                                    print("Your password is too short! ")  # "Your password is too short"
                                else:
                                    # If everything is valid, update the JSON file
                                    ok = True
                                    with open("ID.json", "w") as file:
                                        a = {"username": username, "pasword": pasword1}  # Create a new user
                                        print(objekt["users"])  # Print the current list of users
                                        objekt["users"].append(a)  # Append the new user to the list
                                        print(objekt["users"])  # Print the updated list of users
                                        # Save the updated object back to the JSON file
                                        json.dump(objekt, file, indent=2)
                                        # Notify the user of successful registration
                                        print("úspěšně jste se registrovali")  # "You have successfully registered"
