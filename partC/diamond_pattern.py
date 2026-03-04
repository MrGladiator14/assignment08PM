#!/usr/bin/env python3
"""
Diamond Pattern Generator

This script generates a symmetric diamond pattern using asterisks (*).
The pattern is created using only nested for loops without string multiplication.
"""

def generate_diamond(n):
    """
    Generate a diamond pattern with n rows in the upper triangle.
    
    Args:
        n (int): Number of rows for the upper triangle (including middle row)
    """
    
    # Upper half of the diamond (including middle row)
    for i in range(1, n + 1):
        # Print leading spaces for symmetry
        for space in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for star in range(2 * i - 1):
            print("*", end="")
        
        # Move to next line
        print()
    
    # Lower half of the diamond (excluding middle row)
    for i in range(n - 1, 0, -1):
        # Print leading spaces for symmetry
        for space in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for star in range(2 * i - 1):
            print("*", end="")
        
        # Move to next line
        print()

def main():
    """Main function to get user input and generate diamond pattern."""
    
    try:
        # Get input from user
        n = int(input("Enter the number of rows for the upper triangle: "))
        
        # Validate input
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the diamond pattern
        print("\nDiamond Pattern:")
        generate_diamond(n)
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
