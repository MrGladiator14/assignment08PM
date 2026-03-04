#!/bin/bash

# Test Case 3: Edge cases and visualization testing
echo "=== Test Case 3: Edge Cases and Visualization ==="
echo "Testing: Empty dataset, single transaction, visualization with >10 transactions"
echo

# Create input file for test case 3 (part 1 - empty dataset)
cat > test_input_3a.txt << EOF
done
EOF

echo "Part 1: Empty Dataset Test"
echo "Input: 'done' immediately"
echo "Running transaction analyzer..."
python transaction_analyzer.py < test_input_3a.txt
echo

# Create input file for test case 3 (part 2 - single transaction)
cat > test_input_3b.txt << EOF
25000
credit
Bills
done
EOF

echo "Part 2: Single High-Value Transaction Test"
echo "Input: ₹25000 credit in Bills"
echo "Running transaction analyzer..."
python transaction_analyzer.py < test_input_3b.txt
echo

# Create input file for test case 3 (part 3 - >10 transactions for visualization)
cat > test_input_3c.txt << EOF
1000
credit
Food
2000
debit
Travel
3000
credit
Bills
4000
debit
Other
5000
credit
Food
6000
debit
Travel
7000
credit
Bills
8000
debit
Other
9000
credit
Food
10000
debit
Travel
11000
credit
Bills
12000
debit
Other
done
EOF

echo "Part 3: Visualization Test (12 transactions - should show last 10)"
echo "Input: 12 transactions from ₹1000 to ₹12000"
echo "Running transaction analyzer..."
python transaction_analyzer.py < test_input_3c.txt

echo
echo "=== Expected Results ==="
echo "Part 1: Should show 'No transactions recorded'"
echo "Part 2: Should show 1 transaction, ₹25000 as highest and average"
echo "Part 3: Should show:"
echo "- 12 total transactions"
echo "- Visualization of last 10 transactions (₹3000 to ₹12000)"
echo "- Bar chart with asterisks representing ₹1000 each"
echo "- Highest transaction: ₹12000"
echo "- Average: ₹6500"

# Cleanup
rm -f test_input_3a.txt test_input_3b.txt test_input_3c.txt
