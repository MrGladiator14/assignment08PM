#!/usr/bin/env python3
"""
Test cases for Password Security Suite
Tests the functionality of the password analysis and generation features.
"""

import unittest
import sys
import os

# Add the partA directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'partA'))
from password_security_suite import PasswordSecuritySuite


class TestPasswordSecuritySuite(unittest.TestCase):
    """Test cases for PasswordSecuritySuite class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.suite = PasswordSecuritySuite()
    
    def test_weak_password_analysis(self):
        """Test analysis of a weak password (test case 1)."""
        password = "weak"
        score, rating, missing = self.suite.analyze_strength(password)
        
        # Should have low score and weak rating
        self.assertLess(score, 3)
        self.assertEqual(rating, "Weak")
        
        # Should be missing several criteria
        self.assertIn("Minimum 8 characters", missing)
        self.assertIn("Uppercase letter", missing)
        self.assertIn("Special character", missing)
    
    def test_strong_password_analysis(self):
        """Test analysis of a strong password (test case 2)."""
        password = "StrongP@ssw0rd123!"
        score, rating, missing = self.suite.analyze_strength(password)
        
        # Should have high score and strong rating
        self.assertGreaterEqual(score, 5)
        self.assertIn(rating, ["Strong", "Very Strong"])
        
        # Should have no missing criteria
        self.assertEqual(len(missing), 0)
    
    def test_password_length_scoring(self):
        """Test password length scoring progression (test case 3)."""
        # Test different length thresholds
        short_pass = "Ab1!"  # 4 chars
        medium_pass = "Abcdef12!"  # 9 chars
        long_pass = "Abcdefghijklm12!"  # 17 chars
        
        short_score, _, _ = self.suite.analyze_strength(short_pass)
        medium_score, _, _ = self.suite.analyze_strength(medium_pass)
        long_score, _, _ = self.suite.analyze_strength(long_pass)
        
        # Longer passwords should have higher scores
        self.assertGreater(medium_score, short_score)
        self.assertGreater(long_score, medium_score)
    
    def test_repeated_characters_penalty(self):
        """Test penalty for repeated characters (test case 4)."""
        password_with_repeats = "AAAbbb123!"
        password_without_repeats = "Abc123!@#"
        
        repeat_score, _, repeat_missing = self.suite.analyze_strength(password_with_repeats)
        no_repeat_score, _, no_repeat_missing = self.suite.analyze_strength(password_without_repeats)
        
        # Password with repeats should be penalized
        self.assertIn("No more than 2 repeated characters in a row", repeat_missing)
        self.assertNotIn("No more than 2 repeated characters in a row", no_repeat_missing)
    
    def test_password_generation_length(self):
        """Test password generation with different lengths (test case 5)."""
        # Test minimum length
        min_password = self.suite.generate_password(2)  # Should default to 4
        self.assertEqual(len(min_password), 4)
        
        # Test specific length
        custom_password = self.suite.generate_password(12)
        self.assertEqual(len(custom_password), 12)
        
        # Test that generated password contains all character types
        has_upper = any(c.isupper() for c in custom_password)
        has_lower = any(c.islower() for c in custom_password)
        has_digit = any(c.isdigit() for c in custom_password)
        has_special = any(c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for c in custom_password)
        
        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)
    
    def test_generated_password_strength(self):
        """Test that generated passwords have adequate strength (test case 6)."""
        # Generate multiple passwords and test their strength
        for _ in range(5):
            password = self.suite.generate_password(16)
            score, rating, missing = self.suite.analyze_strength(password)
            
            # Generated passwords should be reasonably strong
            self.assertGreaterEqual(score, 4)
            self.assertNotEqual(rating, "Weak")
            
            # Should meet most criteria
            self.assertLess(len(missing), 3)


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
