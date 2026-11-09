
def deposit(balance, amount, transactions):
    if amount <= 0:
        print("Error: Deposit amount must be greater than zero.")
        return balance

    balance = balance + amount

    record_transaction("deposit", amount, balance, transactions)

    print("Deposit successful.")

    return balance


def withdraw(balance, amount, transactions, total_withdrawn, daily_limit):
    if amount <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
        return balance, total_withdrawn

    if amount > balance:
        print("Error: Insufficient balance.")
        return balance, total_withdrawn

    remaining_limit = daily_limit - total_withdrawn

    if amount > remaining_limit:
        print("Error: Daily withdrawal limit exceeded.")
        print("Remaining withdrawal limit:", remaining_limit)
        return balance, total_withdrawn

    balance = balance - amount
    total_withdrawn = total_withdrawn + amount

    record_transaction("withdrawal", amount, balance, transactions)

    print("Withdrawal successful.")

    return balance, total_withdrawn


def check_balance(balance):
    print("Current balance:", balance, "Birr")


def record_transaction(transaction_type, amount, balance, transactions):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    transactions.append(transaction)


def generate_summary(transactions, balance):
    total_deposited = 0
    total_withdrawn = 0

    print("\n========== TRANSACTION HISTORY ==========")

    for transaction in transactions:
        print("Type:", transaction["type"])
        print("Amount:", transaction["amount"], "Birr")
        print("Balance after:", transaction["balance_after"], "Birr")
        print("-----------------------------------------")

        if transaction["type"] == "deposit":
            total_deposited = total_deposited + transaction["amount"]
        else:
            total_withdrawn = total_withdrawn + transaction["amount"]

    print("\n========== ACCOUNT SUMMARY ==========")
    print("Total deposited:", total_deposited, "Birr")
    print("Total withdrawn:", total_withdrawn, "Birr")
    print("Final balance:", balance, "Birr")
    print("=====================================")


# Main program

balance = 1000
daily_limit = 2000
total_withdrawn = 0

transactions = []

# Multiple transactions
balance = deposit(balance, 500, transactions)

balance, total_withdrawn = withdraw(
    balance, 300, transactions, total_withdrawn, daily_limit
)

balance = deposit(balance, 200, transactions)

balance, total_withdrawn = withdraw(
    balance, 400, transactions, total_withdrawn, daily_limit
)

# Check current balance
check_balance(balance)

# Generate transaction summary
generate_summary(transactions, balance)
