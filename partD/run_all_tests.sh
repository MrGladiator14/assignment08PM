#!/bin/bash

echo "=========================================="
echo "PAYTM TRANSACTION ANALYZER - ALL TESTS"
echo "=========================================="
echo

echo "Running all test cases..."
echo

# Run Test Case 1
echo "▶ Running Test Case 1..."
./test_case_1.sh
echo
echo "----------------------------------------"
echo

# Run Test Case 2
echo "▶ Running Test Case 2..."
./test_case_2.sh
echo
echo "----------------------------------------"
echo

# Run Test Case 3
echo "▶ Running Test Case 3..."
./test_case_3.sh
echo

echo "=========================================="
echo "ALL TESTS COMPLETED"
echo "=========================================="
echo
echo "To run individual tests:"
echo "  ./test_case_1.sh  # Basic functionality"
echo "  ./test_case_2.sh  # Error handling"
echo "  ./test_case_3.sh  # Edge cases and visualization"
