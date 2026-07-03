def main():
    expenses = []
    total = 0.0

    print("Expense Tracker")
    print("Enter expense amounts one by one.")
    print("Type 'q' or 'quit' to finish.\n")

    while True:
        entry = input("Enter expense amount: ").strip().lower()

        if entry in {"q", "quit", "exit"}:
            break

        try:
            amount = float(entry)
            if amount < 0:
                print("Please enter a non-negative amount.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.\n")
            continue

        expenses.append(amount)
        total += amount
        print(f"Added: {amount:.2f}")
        print(f"Running total: {total:.2f}\n")

    print("\nExpense summary")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spent: {total:.2f}")


if __name__ == "__main__":
    main()
