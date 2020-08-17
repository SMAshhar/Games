# This program is going to merge the three programs and generate a single game

# Step 1: The registration process 
# Made a register file by the name of "register.txt"

# # # # # Step 1 - 1: Defining a function/class, each for login and registeration.

import json

def login():
    print("Login")
    name = input("Username : ")
    password = input("Password : ")
    saveFile = name + ".json"
    try:
        with open(saveFile, "r") as f:
            status = json.read(f)
            print(status)
            points = int(status)
    except FileNotFoundError:
        print("User not registered yet")

def register():
    x = True
    while x == True:
        print("Enter new user name")
        name = input("Username : ")
        password = input("Password : ")
        saveFile = name + ".json"
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
                with open("register.json", "a") as f:
                    dict1 = {name : password}
                    json.dump(dict1, f)
                    
            
            
            

# # # # 

    


print("""Enter 'r' to register a new user
        Enter 'l' to login an existing user""")
choice = input()
if choice == "l":
    login()
elif choice == "r":
    register()
    

