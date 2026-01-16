def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{note}\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Expenses ---")
            total = 0
            for line in file:
                amount, category, note = line.strip().split(",")
                print(f"₹{amount} | {category} | {note}")
                total += int(amount)
            print("Total Expense: ₹", total)
    except FileNotFoundError:
        print("No expenses found.")

# Menu for Choose your traget
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
