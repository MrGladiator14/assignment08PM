# assignment08PM

**Project Path:** `github.com:MrGladiator14/assignment08PM`

## Overview

This repository contains a comprehensive Python programming assignment with four distinct parts, each demonstrating different programming concepts and practical applications.

## Project Structure

### Part A: Password Security Suite

- **Files:** `password_security_suite.py`, `test_password_security_suite.py`
- **Purpose:** A comprehensive tool for analyzing password strength and generating secure passwords
- **Features:**
  - Password strength analysis with detailed feedback
  - Secure password generation
  - Strength rating system (Weak/Medium/Strong)
  - Comprehensive test suite

### Part B: Programming Fundamentals

- **Files:** `solution.txt`
- **Purpose:** Detailed solutions to programming fundamentals questions
- **Content:**
  - Differences between `break` and `continue` statements
  - Explanation of `else` clause in loops
  - Code examples and best practices

### Part C: Diamond Pattern Generator

- **Files:** `diamond_pattern.py`, `improved_diamond_pattern.py`
- **Purpose:** Generate symmetric diamond patterns using nested loops
- **Features:**
  - Basic implementation using only nested for loops
  - Improved version with enhanced functionality
  - Pattern generation without string multiplication

### Part D: Transaction Analyzer

- **Files:** `transaction_analyzer.py`, `test_transactions.py`, multiple test scripts
- **Purpose:** Paytm-style transaction analytics tool
- **Features:**
  - Transaction input and categorization
  - Credit/debit tracking
  - Category-wise spending analysis (Food, Travel, Bills, Other)
  - Comprehensive test suite with multiple test cases

## Technical Details

- **Python Version:** >=3.12
- **Package Manager:** UV (with `uv.lock` file)
- **Project Structure:** Modular design with separate directories for each part
- **Testing:** Comprehensive test suites for Parts A and D

## Getting Started

1. Clone the repository:

   ```bash
   git clone github.com:MrGladiator14/assignment08PM
   ```
2. Install dependencies:

   ```bash
   uv sync
   ```
3. Run individual parts:

   ```bash
   # Part A - Password Security Suite
   python partA/password_security_suite.py

   # Part C - Diamond Pattern
   python partC/diamond_pattern.py

   # Part D - Transaction Analyzer
   python partD/transaction_analyzer.py
   ```

## Main Entry Point

The `main.py` file serves as a simple entry point that prints a welcome message for the assignment.
