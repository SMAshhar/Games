# # This program is going to merge the three programs and generate a single game

# # Step 1: The registration process 
# # Made a register file by the name of "register.json".

# # # # # # Step 1 - 1: Defining a function for registeration.

import json
name = ""
password = ""

def register():
    x = True
    while x == True:
        print("###########################################################")
        print("Enter new user name")                # asking for a New username and password
        name = input("Username : ")
        password = input("Password : ")             # stll don't know how to camoflage password. Will add the feature later
        print("###########################################################")
        z = 0
        saveFile = name + ".txt"                    # for every new user, there will be a separate savefile
        with open("register.json") as f:            # Each username with password will be stored in this jason file                        
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
                    data = json.load(f)             # Adding the new provided username in the "register.json" file
                    dict1 = {name : password}
                    data.update(dict1)
                    f.seek(0)
                    json.dump(data, f)
                with open(saveFile, "w") as f:
                    f.write("0")                    # Making a new save file which will store points for each user
                    print("Savefile made")
                    break

# # # # # # Step 1 - 2: Defining a function for loging in

def login(name, password):                          # Funciton for loging in. Here positional arguments are needed
    login = False
    while login == False:
        saveFile = name + ".txt"                    # Making a variable to help recall the save file for that perticuler user
        with open("register.json", "r") as j:
            check = json.load(j)                 
            if name in check.keys():                # Checking if username has been registered
                for key, value in check.items():               # Checking for correct username and password.               
                    if key == name and value == password:                 
                        try:
                            with open(saveFile, "r") as f:      # Recalling points from user's savefile
                                status = f.read()
                                print(status)
                                global points
                                points = int(status)
                                
                        except FileNotFoundError:
                            print("SaveFile not found.")
                            with open(saveFile, "w") as f:            # If save file is deleted. A new one has to be made
                                print("New saev file made.")
                        finally:
                            login = True
                            return login                              # If all is cleared. User is logged in
                    else:
                        print("Wrong username or password")
            else:
                print("Use not registered, please register")
                return register()

# # Step 2: Initiating the game menu and loging in with guide.

loginIn = False
while loginIn == False:                             # The first printed line, will ask the user if he wants to login or register
    print("""Enter 'r' to register a new user
Enter 'l' to login an existing user""")
    choice = input()
    if choice.lower() == "l":
        print("###########################################################")
        name = input("Username : ")
        password = input("Password : ")
        print("###########################################################")
        login(name, password)                       # This line will call the Login function if the user enters "l"
        loginIn = True
    elif choice.lower() == "r":
        register()                                  # This line will call the register function if the user enters "r"
        print("Registration is complete, continue to login")
        print("###########################################################")

# # Step 3: Charactor Selection

if loginIn == True:                                  # If login is successful, this piece will initiate the charactor selection.
    print("""
            Select your charactor
            1. Warrior
            2. Hunter
            3. Priest
    """)

# # Step 4: Importing the user chosen charactor and start the game

    selection = int(input("\t\tEnter number : "))
    if selection == 1:
        import Warrior                              # If Warrior is selected, we will be importing warrior module.
        saveFile = name +".txt"                     # Making the save file's name so that we can call it later on
        print(Warrior.points)                       # Printing the total points user took from this session
        with open(saveFile, "w") as f:              # Adding the points from this session to the last total points, making a new total
            f.write(str(points + Warrior.points))
        print("Your total points are : ", points + Warrior.points)      # Game's last line
    elif selection == 2:
        import Hunter                               # All the same if Hunter class is selected
        saveFile = name +".txt"
        print(Hunter.points)
        with open(saveFile, "w") as f:
            f.write(str(points + Hunter.points))
        print("Your total points are : ", points + Hunter.points)
    elif selection == 3:
        import gamePriest                           # All the same if Priest class is selected
        saveFile = name +".txt"
        print(gamePriest.points)
        with open(saveFile, "w") as f:
            f.write(str(points + gamePriest.points))
        print("Your total points are : ", points + gamePriest.points)    
       
