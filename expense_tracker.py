# Expense Tracker

expenses = []

while True:
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

choice = input("Choose an option (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

expenses.append
(
  {
            "amount": amount,
            "category": category,
            "description": description
  }
)

           print("Expense added successfully!")

elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for exp in expenses:
                print(f"{exp['category']} - ₹{exp['amount']} : {exp['description']}")

    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Exiting Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
