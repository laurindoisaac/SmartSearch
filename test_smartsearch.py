# test_smartsearch.py
"""
Tests for SmartSearch module.
"""

import unittest
from smartsearch import SmartSearch

class TestSmartSearch(unittest.TestCase):
    """Test cases for SmartSearch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartSearch()
        self.assertIsInstance(instance, SmartSearch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartSearch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
