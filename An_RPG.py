# # This program is going to merge the three programs and generate a single game

# # Step 1: The registration process 
# # Made a register file by the name of "register.txt"

# # # # # # Step 1 - 1: Defining a function/class, each for login and registeration.

import json

def login():
    print("Login...")
    print("###########################################################")
    name = input("Username : ")
    password = input("Password : ")
    print("###########################################################")
    saveFile = name + ".txt"

    with open("register.json", "r") as j:
        check = json.load(j)
        if name in check.keys():
            for key, value in check.items():
                if key == name and value == password:                 
                    try:
                        with open(saveFile, "r") as f:
                            status = f.read()
                            print(status)
                            points = int(status)
                    except FileNotFoundError:
                        print("SaveFile not found")            # we can repeat a new savefile making process here if the file is deleted somehow


def register():
    x = True
    while x == True:
        z = 0
        print("###########################################################")
        print("Enter new user name")
        name = input("Username : ")
        password = input("Password : ")
        print("###########################################################")
        saveFile = name + ".txt"
        with open("register.json") as f:                       
            check = json.load(f)
            print(check)
            for a in check:                         # check for name availability
                if a == name:
                    print("Name has already been taken")
                    z = 1
                    break
            if z == 1:
                continue
            else:
                with open("register.json", "r+") as f:
                    data = json.load(f)
                    dict1 = {name : password}
                    data.update(dict1)
                    f.seek(0)
                    json.dump(data, f)
                with open(saveFile, "w") as f:
                    f.write("0")
                    print("Savefile made")
                    break


loginIn = False
while loginIn == False:                    
    print("""Enter 'r' to register a new user
    Enter 'l' to login an existing user""")
    choice = input()
    if choice == "l":
        login()
        loginIn = True
    elif choice == "r":
        register()
        print("Registration is complete, continue to login")
        print("###########################################################")
        login()
        


