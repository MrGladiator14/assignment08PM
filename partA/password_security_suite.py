#!/usr/bin/env python3
"""
Password Security Suite
A comprehensive tool for analyzing password strength and generating secure passwords.
"""

import random
import string
import re


class PasswordSecuritySuite:
    """Main class for password security operations."""
    
    def __init__(self):
        self.strength_ratings = {
            0: "Weak",
            1: "Weak", 
            2: "Weak",
            3: "Medium",
            4: "Medium",
            5: "Strong",
            6: "Strong"
        }
    
    def analyze_strength(self, password):
        """
        Analyze password strength and return score with detailed feedback.
        
        Args:
            password (str): Password to analyze
            
        Returns:
            tuple: (score, rating, missing_criteria)
        """
        score = 0
        missing_criteria = []
        
        length = len(password)
        if length >= 8:
            score += 1
        else:
            missing_criteria.append("Minimum 8 characters")
            
        if length >= 12:
            score += 1
        if length >= 16:
            score += 1
        
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)
        
        if has_upper:
            score += 1
        else:
            missing_criteria.append("Uppercase letter")
            
        if has_lower:
            score += 1
        else:
            missing_criteria.append("Lowercase letter")
            
        if has_digit:
            score += 1
        else:
            missing_criteria.append("Digit")
            
        if has_special:
            score += 1
        else:
            missing_criteria.append("Special character")
        
        repeated_pattern = re.compile(r'(.)\1{2,}')
        if not repeated_pattern.search(password):
            score += 1
        else:
            missing_criteria.append("No more than 2 repeated characters in a row")
        
        if score >= 7:
            rating = "Very Strong"
        else:
            rating = self.strength_ratings.get(score, "Weak")
        
        return score, rating, missing_criteria
    
    def generate_password(self, length):
        """
        Generate a random password of specified length.
        
        Args:
            length (int): Desired password length
            
        Returns:
            str: Generated password
        """
        if length < 4:
            length = 4  # Minimum viable length
        
        # Ensure we have at least one of each character type
        chars = []
        chars.append(random.choice(string.ascii_uppercase))
        chars.append(random.choice(string.ascii_lowercase))
        chars.append(random.choice(string.digits))
        chars.append(random.choice(string.punctuation))
        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        for _ in range(length - 4):
            chars.append(random.choice(all_chars))
        
        random.shuffle(chars)
        
        return ''.join(chars)
    
    def display_analysis(self, password):
        """Display password analysis results in a user-friendly format."""
        score, rating, missing = self.analyze_strength(password)
        
        print(f"\n{'='*50}")
        print(f"Password Analysis Results")
        print(f"{'='*50}")
        print(f"Password: {'*' * len(password)}")
        print(f"Score: {score}/7")
        print(f"Rating: {rating}")
        
        if missing:
            print(f"\nMissing Criteria:")
            for criterion in missing:
                print(f"  • {criterion}")
        else:
            print(f"\n✓ All criteria met!")
        
        print(f"{'='*50}")
        
        return score
    
    def run_strength_analyzer(self):
        """Run the password strength analyzer with re-prompting loop."""
        print("\n" + "="*50)
        print("PASSWORD STRENGTH ANALYZER")
        print("="*50)
        print("Enter a password to analyze its strength.")
        print("You will be re-prompted until the password scores 5 or higher.\n")
        
        while True:
            password = input("Enter password: ").strip()
            
            if not password:
                print("Password cannot be empty. Please try again.")
                continue
            
            score = self.display_analysis(password)
            
            if score >= 5:
                print("\n✓ Strong password achieved!")
                break
            else:
                print("\n❌ Password is too weak. Please try again.")
    
    def run_generator(self):
        """Run the random password generator."""
        print("\n" + "="*50)
        print("RANDOM PASSWORD GENERATOR")
        print("="*50)
        
        while True:
            try:
                length_input = input("Enter desired password length (4-32): ").strip()
                length = int(length_input)
                
                if length < 4 or length > 32:
                    print("Please enter a length between 4 and 32.")
                    continue
                
                password = self.generate_password(length)
                print(f"\nGenerated Password: {password}")
                
                score, rating, _ = self.analyze_strength(password)
                print(f"Strength Score: {score}/7")
                print(f"Rating: {rating}")
                
                break
                
            except ValueError:
                print("Please enter a valid number.")
    
    def run_menu(self):
        """Run the main menu interface."""
        print("="*60)
        print("    PASSWORD SECURITY SUITE")
        print("="*60)
        print("1. Password Strength Analyzer")
        print("2. Random Password Generator")
        print("3. Exit")
        print("="*60)
        
        while True:
            choice = input("\nSelect an option (1-3): ").strip()
            
            if choice == "1":
                self.run_strength_analyzer()
            elif choice == "2":
                self.run_generator()
            elif choice == "3":
                print("\nThank you for using Password Security Suite!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
            
            # Show menu again after each operation (except exit)
            if choice != "3":
                print("\n" + "="*60)
                print("    PASSWORD SECURITY SUITE")
                print("="*60)
                print("1. Password Strength Analyzer")
                print("2. Random Password Generator")
                print("3. Exit")
                print("="*60)


def main():
    """Main entry point for the application."""
    suite = PasswordSecuritySuite()
    suite.run_menu()


if __name__ == "__main__":
    main()
