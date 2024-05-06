
file = open("ID.txt","r")
data = file.read()
print(data)
file.close()


ok = False

username = input("write username:  ")
if username in data: 
    pasword = input("write pasword: ")
    if pasword in data:
        print("jste přihlášená")
    else:
        next
if pasword not in data:
    print("wrong pasword! ")
    next
    username = input("please, write your new username: ")
    while not ok:
        if username in data:
            continue
        else: 
            if len(username) <=6:
                print("you have to short password! ")
                continue
            while not ok:
                pasword = input("write password: ")
                if pasword not in username:
                    print(" worng password!")
                    pasword = input("Please, write your new password: ")
                    pasword1 = input("Please, write again your new password: ")
                    while not ok:
                        if pasword in data:
                            continue
                        else:
                            if pasword != pasword1:
                                print("you dont have same password!! :")
                                continue
                            else:
                                if len(pasword and pasword1) <=6:
                                    print("you have a short new password!! ")
                                else:
                                    if True:
                                        ok = True
                                        file = open("ID.txt", "a")
                                        file.write("\n"+ username + "," + pasword1)
                                        file.close()
                                        print("you have successfully logged in. :)")
                                            




                                