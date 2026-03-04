# Paytm Transaction Analyzer
transactions = []
categories = {"Food": 0, "Travel": 0, "Bills": 0, "Other": 0}

print("--- Paytm Backend Analytics Tool ---")
print("Enter 'done' to generate report.\n")

while True:
    entry = input("Enter amount (or 'done'): ").lower()
    if entry == 'done':
        break
    
    try:
        amount = float(entry)
        if amount <= 0:
            print("Error: Amount must be positive. Please try again.")
            continue
    except ValueError:
        print("Error: Please enter a valid numeric amount.")
        continue
    
    while True:
        trans_type = input("Enter type (credit/debit): ").lower().strip()
        if trans_type in ['credit', 'debit']:
            break
        else:
            print("Error: Type must be 'credit' or 'debit'. Please try again.")
    
    while True:
        category = input("Enter category (Food/Travel/Bills/Other): ").capitalize().strip()
        if category in categories:
            break
        else:
            print(f"Error: Category must be one of {list(categories.keys())}. Please try again.")
    
    transaction = {
        'amount': amount,
        'type': trans_type,
        'category': category
    }
    transactions.append(transaction)
    
    categories[category] += amount
    
    print(f"Transaction recorded: ₹{amount:.2f} {trans_type} in {category}\n")

print("\n" + "="*50)
print("PAYTM TRANSACTION ANALYSIS REPORT")
print("="*50)

if not transactions:
    print("No transactions recorded.")
else:
    total_credits = sum(t['amount'] for t in transactions if t['type'] == 'credit')
    total_debits = sum(t['amount'] for t in transactions if t['type'] == 'debit')
    net_balance = total_credits - total_debits
    
    high_value_transactions = [t for t in transactions if t['amount'] > 10000]
    
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Credits: ₹{total_credits:.2f}")
    print(f"Total Debits: ₹{total_debits:.2f}")
    print(f"Net Balance: ₹{net_balance:.2f}")
    
    if high_value_transactions:
        print(f"High-Value Transactions (>₹10,000): {len(high_value_transactions)}")
        for t in high_value_transactions:
            print(f"  - ₹{t['amount']:.2f} ({t['type']}) in {t['category']}")
    else:
        print("High-Value Transactions (>₹10,000): None")
    
    if transactions:
        highest_transaction = max(transactions, key=lambda x: x['amount'])
        average_transaction = sum(t['amount'] for t in transactions) / len(transactions)
        
        print(f"Highest Transaction: ₹{highest_transaction['amount']:.2f} ({highest_transaction['type']}) in {highest_transaction['category']}")
        print(f"Average Transaction Value: ₹{average_transaction:.2f}")
    
    print("\nCategory-wise Breakdown:")
    for category, total in categories.items():
        if total > 0:
            print(f"  {category}: ₹{total:.2f}")
    
    print("\n" + "="*50)
    print("LAST 10 TRANSACTIONS VISUALIZATION")
    print("="*50)
    
    last_10_transactions = transactions[-10:] if len(transactions) > 10 else transactions
    
    for i, trans in enumerate(last_10_transactions, 1):
        bar_length = int(trans['amount'] // 1000)  # Each * represents ₹1,000
        bar = '*' * bar_length
        print(f"{i:2d}. ₹{trans['amount']:7.2f} {trans['type']:6s} {trans['category']:6s} | {bar}")

print("\n" + "="*50)
print("Thank you for using Paytm Backend Analytics Tool!")
print("="*50)
