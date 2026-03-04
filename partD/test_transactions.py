# Paytm Transaction Analyzer - Test Script

# This file contains sample test data and expected outputs for verification

print("=== TESTING PAYTM TRANSACTION ANALYZER ===")
print("Run the following test sequence to verify functionality:")
print()

test_data = [
    # (amount, type, category)
    ("5000", "credit", "Food"),
    ("3000", "debit", "Travel"),
    ("15000", "credit", "Bills"),  # High-value transaction
    ("2000", "debit", "Food"),
    ("12000", "debit", "Travel"),  # High-value transaction
    ("7500", "credit", "Other"),
    ("4500", "debit", "Bills"),
    ("8000", "credit", "Food"),
    ("9000", "debit", "Other"),
    ("11000", "credit", "Bills"),  # High-value transaction
    ("6000", "debit", "Travel"),
    ("done", "", "")
]

print("Test Data Sequence:")
for i, (amount, trans_type, category) in enumerate(test_data[:-1], 1):
    print(f"{i:2d}. Amount: {amount}, Type: {trans_type}, Category: {category}")

print(f"{len(test_data):2d}. Amount: done (to exit)")
print()

print("Expected Results:")
print("- Total Transactions: 11")
print("- Total Credits: ₹51500.00")
print("- Total Debits: ₹42500.00")
print("- Net Balance: ₹9000.00")
print("- High-Value Transactions: 3")
print("- Highest Transaction: ₹15000.00")
print("- Average Transaction: ₹8545.45")
print("- Category Breakdown:")
print("  - Food: ₹15000.00")
print("  - Travel: ₹21000.00") 
print("  - Bills: ₹30500.00")
print("  - Other: ₹22500.00")

print()
print("To run the actual program:")
print("python transaction_analyzer.py")
print()
print("Then enter the test data above when prompted.")
