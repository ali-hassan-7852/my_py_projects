def register():
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", 'a') as f:
        f.write(f"{user_name}:{password}\n")
def login():
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    with open("users.txt", 'r') as f:
        users = f.readlines()
        for user in users:
            parts = user.strip().split(":", 1)
            if len(parts) == 2:
                user_name, password = parts
            if user_name == user_username and password == user_password:
                print("Login successful!")
                return True
        print("Invalid username or password. Please try again.")
        return False
while True:
    print("\nLogin System")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        register()
    elif choice == "2":
        if login():
            break
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")