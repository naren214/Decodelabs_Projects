import math


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
            new_total = total + amount
            if not math.isfinite(amount) or amount < 0 or not math.isfinite(new_total):
                print("Please enter a finite, non-negative amount that keeps the total finite.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.\n")
            continue

        expenses.append(amount)
        total = new_total
        print(f"Added: {amount:.2f}")
        print(f"Running total: {total:.2f}\n")

    print("\nExpense summary")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spent: {total:.2f}")


if __name__ == "__main__":
    main()
