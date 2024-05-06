import json
with open("ID.json","r") as file:
    data = file.read()
    objekt = json.loads(data)
    print(objekt)
    

# načtení dat z Json a vypsání uživatelů bez USERS
ok = False

username = input("prihlasovaci jmeno: ")
if username in data: 
    pasword = input("zadejte heslo: ")
    if pasword in data:
        print("jste přihlášená")
    else:
        next
if username not in data:
    print("zadali jste špatné jméno! ")
    next
    username = input("zadejte nové přihlašovací j1méno:")
    while not ok:
        if username in data:
            continue
        else: 
            if len(username) <=6:
                print("máte moc krátké jméno")
                continue
            while not ok:
                pasword = input("heslo: ")
                if pasword not in username:
                    print(" zadali jste špatné heslo!")
                    pasword = input("zadej nové přihlašovací heslo: ")
                    pasword1 = input("zadej znova nové přihlašovací heslo: ")
                    while not ok:
                        if pasword in data:
                            continue
                        else:
                            if pasword != pasword1:
                                print("nemáte stejné hesla :")
                                break
                            else:
                                if len(pasword and pasword1) <=6:
                                    print("máte moc krátké heslo ")
                                else:
                                    if True:
                                        ok = True
                                        with open("ID.json","w") as file:
                                            a = {"username":username, "pasword": pasword1}
                                            print(objekt["users"])
                                            objekt["users"].append(a)
                                            print(objekt["users"])
                                            json.dump(objekt, file, indent= 2 )
# načtení dat z Json a vypsání uživatelů bez USERS
                                            print("úspěšně jste se registrovali ")
                                            