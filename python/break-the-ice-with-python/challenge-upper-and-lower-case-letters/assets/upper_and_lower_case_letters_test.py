import unittest
import sys
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from upper_and_lower_case_letters import upper_and_lower_case_letters

class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard input and output to buffer
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # Input test data
        test_input = 'Hello World\n'
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # Run the code
        upper_and_lower_case_letters()

        # Restore standard input and output
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = 'UPPER CASE 2\nLOWER CASE 8\n'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
