username = input("Enter username: ")
valid = True
---------------------------
# Rule 1: Length check
---------------------------
if len(username) < 5 or len(username) > 15:
    print("Invalid username")
    print("- Username must be between 5 and 15 characters")
valid = False
---------------------------
# Rule 2: Should not start with a number
---------------------------
if username[0].isdigit():
    print("Invalid username")
    print("- Username should not start with a number")
valid = False
---------------------------
# Rule 3: Only letters, numbers, underscore allowed
---------------------------
for char in username:
    if not (char.isalnum() or char == "_"):
        print("Invalid username")
        print("- Username can contain only letters, numbers, and underscores")
valid = False
       
        break
---------------------------
# Final result
---------------------------
if valid:
    print("Valid username ✅")
