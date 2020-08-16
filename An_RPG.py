# This program is going to merge the three programs and generate a single game

# Step 1: The registration process

# # # # # Step 1 - 1: Defining a function/class, each for login and registeration.

def login():
    name = input("Username : ")
    password = input("Password : ")
    try:
        with open(name".txt", "a") as f:
    except FileNotFoundError:
        print("User not registered yet")
    except:
        print("An error has occured. Please try again")




print("""Enter 'r' to register a new user
        Enter 'l' to login an existing user""")
choice = input()
if choice == "l":
    print("Login: ")
    name = input("Username : ")
    password = input("Password : ")
    try:
        with open(name".txt", "a") as f:
    except FileNotFoundError:
        print("User not registered yet")
    except:
        print("An error has occured. Please try again")
    


regName = input()