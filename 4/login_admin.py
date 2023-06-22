def login(password,username="Admin"):
    

    if password==123:
        print("Login successful!")
    else:
        print("Invalid password.")

x=int(input("Enter the password: "))
login(x)