#!/bin/bash

# Test Case 1: Basic functionality with mixed transactions
echo "=== Test Case 1: Basic Mixed Transactions ==="
echo "Testing: Normal credits/debits, high-value detection, category tracking"
echo

# Create input file for test case 1
cat > test_input_1.txt << EOF
5000
credit
Food
3000
debit
Travel
15000
credit
Bills
2000
debit
Food
12000
debit
Travel
done
EOF

# Run the transaction analyzer with test input
echo "Input transactions:"
echo "1. ₹5000 credit (Food)"
echo "2. ₹3000 debit (Travel)" 
echo "3. ₹15000 credit (Bills) - High Value"
echo "4. ₹2000 debit (Food)"
echo "5. ₹12000 debit (Travel) - High Value"
echo

echo "Running transaction analyzer..."
python transaction_analyzer.py < test_input_1.txt

echo
echo "=== Expected Results ==="
echo "Total Transactions: 5"
echo "Total Credits: ₹20000.00"
echo "Total Debits: ₹17000.00"
echo "Net Balance: ₹3000.00"
echo "High-Value Transactions: 2 (₹15000, ₹12000)"
echo "Category Breakdown:"
echo "  Food: ₹7000.00 (₹5000 credit - ₹2000 debit)"
echo "  Travel: ₹15000.00 (₹12000 debit)"
echo "  Bills: ₹15000.00 (₹15000 credit)"
echo "  Other: ₹0.00"

# Cleanup
rm -f test_input_1.txt
