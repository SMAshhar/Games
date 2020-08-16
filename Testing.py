def login():
    name = input("Username : ")
    password = input("Password : ")
    try:
        with open("name.txt", "a") as f:
    except:
        print("User not registered yet")
    
login()