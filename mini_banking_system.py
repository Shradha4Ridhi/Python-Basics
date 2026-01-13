# mini_banking_system.py

balance = 0

def deposit(amount):
    global balance
    balance += amount
         print(f"Deposited ₹{amount}. Current balance: ₹{balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
         print(f"Withdrew ₹{amount}. Current balance: ₹{balance}")
    else:
         print("Insufficient balance.")

def check_balance():
       print(f"Current balance: ₹{balance}")

if __name__ == "__main__":
       deposit(1000)
       withdraw(300)
       check_balance()
