# tests.py

import unittest

# Discover and run all test cases in the "tests" folder
if __name__ == "__main__":
    # Specify the folder where tests are located
    suite = unittest.defaultTestLoader.discover(start_dir="src/tests", pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)
