import random
import string
users=[]
passwords=[]
print("----Welcome to Password Manager----")
print("1. Add a user name & Password: ")
print("2. Remove a user name & Password: ")
print("3. View all user names and passwords: ")
print("4. Change a user name & Password: ")
print("5. Generate a random password: ")
print("6. Exit")
while True:
    choice = input("Enter your choice: ")
    if choice=="1":
        user=input("Enter your user name: ")
        password=input("Enter your password: ")
        if user in users:
            print("Username already taken!")
        else:
            users.append(user)
            passwords.append(password)
            print(f"User added successfully! ")

    elif choice=="2":
        user=input("Enter your user name to remove: ")
        if user in users:
            index=users.index(user)
            users.pop(index)
            passwords.pop(index)
            print(f"User removed successfully! ")
        else:
            print("No User found!")

    elif choice=="3":
        for i in range (len(users)):
            print(f"Username: {users[i]} | Password: {passwords[i]}")

    elif choice =="4":
        user=input("Enter your user name to change: ")
        if user in users:
            index=users.index(user)
            new_user_name=input("Enter new user name: ")
            new_user_password=input("Enter new user's password: ")
            users[index]=new_user_name
            passwords[index]=new_user_password
            print(f"User Name & Password changed successfully! ")
        else:
            print(f"No User found!")
    elif choice=="5":
        length = int(input("Enter password length: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""
        for i in range(length):
            password += random.choice(characters)
        print("Generated Password:", password)
    elif choice=="6":
        print("Thank you for using Password Manager")
        break
    else:
        print("Invalid Choice!")


