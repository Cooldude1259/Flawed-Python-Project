def Usr(user):
    def wrong():
        print("Username or password incorrect!")
    if user == "User1":
        user = "1"
    elif user == "User2":
        user = "2"
    elif user == "User3":
        user = "3"
    else:
        wrong()
def pswd(passwd, user):
    def login():
        print("Login successful!")
    if user == "1":
        if passwd == "password1":
            login()
        else:
            wrong()
    elif user == "2":
        if passwd == "password2":
            login()
        else:
            wrong()
    elif user == "3":
        if passwd == "password3":
            login()
        else:
            wrong()
            
print("Hello!")
print("Please log in:")
user = input("Enter your username: ")
passwd = input("Enter your password: ")

