# This program is going to merge the three programs and generate a single game

# Step 1: The registration process 
# Made a register file by the name of "register.txt"

# # # # # Step 1 - 1: Defining a function/class, each for login and registeration.

import json

def login():
    print("Login")
    name = input("Username : ")
    password = input("Password : ")
    saveFile = name + ".txt"
    try:
        with open(saveFile, "r") as f:
            status = f.read()
            print(status)
            points = int(status)
    except FileNotFoundError:
        print("User not registered yet")

def register():
    x = True
    while x == True:
        z = 0
        print("Enter new user name")
        name = input("Username : ")
        password = input("Password : ")
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
                    break
                    
print("""Enter 'r' to register a new user
Enter 'l' to login an existing user""")
choice = input()
if choice == "l":
    login()
elif choice == "r":
    register()
    

