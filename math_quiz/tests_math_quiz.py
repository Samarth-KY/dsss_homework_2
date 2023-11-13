import unittest
from math_quiz import generate_random_int, select_random_operation, math_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_int(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operation(self):
        """
        Test the select_random_operation function to ensure it returns a valid math operation.
        """
        valid_operations_set = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operation = select_random_operation()
            self.assertTrue(operation in valid_operations_set)

    def test_math_operation(self):
        """
        Test the math_operation function with some test cases.
        """
        test_cases = [
                (5, 2, '+', '5 + 2', 7),(7,3,'-','7 - 3',4),(2,3,'*','2 * 3',6)
            ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = math_operation(num1, num2, operator)
                
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
