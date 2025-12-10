# test_webhookrelay.py
"""
Tests for WebhookRelay module.
"""

import unittest
from webhookrelay import WebhookRelay

class TestWebhookRelay(unittest.TestCase):
    """Test cases for WebhookRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebhookRelay()
        self.assertIsInstance(instance, WebhookRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebhookRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
