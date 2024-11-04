# tests/test_chat.py

import unittest
from src.user_chat.chat import chat_loop
from unittest.mock import patch

class TestChatLoop(unittest.TestCase):
    
    @patch("builtins.input", side_effect=["what system am i using?", "exit"])
    @patch("builtins.print")
    def test_system_info(self, mock_print, mock_input):
        # Run the chat loop
        chat_loop()
        
        # Check if the expected output was printed
        expected_output = [
            "Hi! I'm a Artie. your AI Assistant! Type 'exit' to quit.",
            "Artie: You are using Linux.",
            "Artie: Goodbye!"
        ]
        
        # Extract only Artie's responses from the mock print calls
        all_prints = [args[0] for args, _ in mock_print.call_args_list]
        
        # Assert that the output matches the expected sequence
        self.assertEqual(all_prints, expected_output)

if __name__ == "__main__":
    unittest.main()
