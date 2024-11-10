import unittest
from math_quiz import generate_random_number, generate_random_operator, create_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test with a large sample size
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the operator returned is one of the expected values
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test with a large sample size
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators)

    def test_create_math_problem(self):
        # Test if the math problem generation is correct
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            (7, 1, '+', '7 + 1', 8),
            (9, 5, '-', '9 - 5', 4)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem_str, correct_answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem_str, expected_problem)
            self.assertEqual(correct_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
