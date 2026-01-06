password = input("Enter your password: ")
score = 0
---------------------
 # Rule 1: Length
---------------------
if len(password) >= 8:
    score += 1
---------------------
# Rule 2: Digit
---------------------
has_digit = False
for char in password:
if char.isdigit():
        has_digit = True
break
      if has_digit:
      score += 1
---------------------
# Rule 3: Uppercase
---------------------
has_upper = False
for char in password:
   if char.isupper():
        has_upper = True
   break

if has_upper:
    score += 1
---------------------
# Rule 4: Special character
---------------------
special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>/?"
has_special = False

for char in password:
    if char in special_chars:
        has_special = True
        break

if has_special:
    score += 1
---------------------
# Result
---------------------
if score <= 1:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
