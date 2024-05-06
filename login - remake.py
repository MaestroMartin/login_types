
ID = {"martin" :1234568, "adam" :1234} 

print(ID)

username = str
pasword = int

username = ID.keys 
pasword = ID.values 

# username == pasword

username = input("prihlasovaci jmeno: ") 
if username in ID:
    print( "správné jmeno")
else:
    print("špatné jmeno")


pasword = input("heslo: ")
if pasword not in username:
    print("zadali jste špatné heslo")
else:
    print("prihlasovani")

def pasword():
    for pasword in ID.values(int):
        if pasword == False:
            if username == False:
                return username
            


        