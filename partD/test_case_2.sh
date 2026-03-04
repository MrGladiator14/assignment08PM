#!/bin/bash

# Test Case 2: Error handling and validation
echo "=== Test Case 2: Input Validation and Error Handling ==="
echo "Testing: Invalid amounts, invalid transaction types, invalid categories"
echo

# Create input file for test case 2
cat > test_input_2.txt << EOF
abc
-500
0
5000
credit
InvalidCategory
Food
3000
invalid_type
debit
Travel
done
EOF

# Run the transaction analyzer with test input
echo "Input sequence with errors:"
echo "1. 'abc' - Invalid amount (non-numeric)"
echo "2. '-500' - Invalid amount (negative)"
echo "3. '0' - Invalid amount (zero)"
echo "4. '5000' - Valid amount"
echo "5. 'credit' - Valid type"
echo "6. 'InvalidCategory' - Invalid category"
echo "7. 'Food' - Valid category"
echo "8. '3000' - Valid amount"
echo "9. 'invalid_type' - Invalid transaction type"
echo "10. 'debit' - Valid type"
echo "11. 'Travel' - Valid category"
echo "12. 'done' - Exit"
echo

echo "Running transaction analyzer..."
python transaction_analyzer.py < test_input_2.txt

echo
echo "=== Expected Results ==="
echo "Should show error messages for:"
echo "- Non-numeric amount 'abc'"
echo "- Negative amount '-500'"
echo "- Zero amount '0'"
echo "- Invalid category 'InvalidCategory'"
echo "- Invalid transaction type 'invalid_type'"
echo "Should successfully record:"
echo "- ₹5000 credit in Food"
echo "- ₹3000 debit in Travel"
echo "Final totals: 2 transactions, ₹5000 credit, ₹3000 debit, ₹2000 net balance"

# Cleanup
rm -f test_input_2.txt
