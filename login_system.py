# Simple Login System

correct_username = "student"
correct_password = "python123"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
               print("Login successful!")
    break
   
else:
        attempts -= 1
             print("Incorrect username or password.")
             print("Attempts left:", attempts)

if attempts == 0:
    print("Too many failed attempts. Access denied.")
