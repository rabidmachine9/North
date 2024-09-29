import unittest
from pforth import ForthInterpreter  # Assuming the interpreter is in pif.py

class TestForthInterpreter(unittest.TestCase):

    def setUp(self):
        """Set up a new interpreter instance before each test."""
        self.interpreter = ForthInterpreter()

    def test_addition(self):
        program = "5 10 +"
        result = self.interpreter.run(program)
        self.assertEqual(result, 15.0)
    
    def test_addition_multi(self):
        program = "5 10 5 +"
        result = self.interpreter.run(program)
        self.assertEqual(result, 20.0)
    
    
    def test_comments(self):
        program = "5 10 5 + \ this is a random comment"
        result = self.interpreter.run(program)
        self.assertEqual(result, 20.0)


    def test_addition_multi2(self):
        program = "5 10 5 4 +"
        result = self.interpreter.run(program)
        self.assertEqual(result, 24.0)

    def test_subtraction(self):
        program = "20 5 -"
        result = self.interpreter.run(program)
        self.assertEqual(result, 15.0)

    def test_function_definition(self):
        program = ": square dup * ; 5 square"
        result = self.interpreter.run(program)
        self.assertEqual(result, 25.0)

    def test_variable_assignment(self):
        program = "5 :x 10 :y x y +"
        result = self.interpreter.run(program)
        self.assertEqual(result, 15.0)

    def test_multiply(self):
        program = "5 5 *"
        result = self.interpreter.run(program)
        self.assertEqual(result, 25.0)

    def test_multiply_multi(self):
        program = "5 5 5 *"
        result = self.interpreter.run(program)
        self.assertEqual(result, 125.0)

    def test_divide(self):
        program = "5 5 /"
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)

    def test_modulo(self):
        program = "6 5 %"
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)

    def test_logic_equals(self):
        program = "1 2 ="
        result = self.interpreter.run(program)
        self.assertEqual(result, 0.0)

    def test_logic_not_equals(self):
        program = "1 2 <>"
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)

    def test_logic_and(self):
        program = "1 2 and"
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)

    def test_boolean_not(self):
        program = "1 not"
        result = self.interpreter.run(program)
        self.assertEqual(result, 0.0)
    
    def test_boolean_not_2(self):
        program = "0 not"
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)

    def test_greater_than(self):
        program = "5 6 >"
        result = self.interpreter.run(program)
        self.assertEqual(result, 0.0)

    def test_less_than(self):
        program = "5 6 <"
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)

    def test_if_positive(self):
        program = "5 0 > if 1 else 0 then"  # Should execute the 'if' part and return 1
        result = self.interpreter.run(program)
        self.assertEqual(result, 1.0)  # Expecting to return 1.0 for true condition

    def test_if_zero(self):
        program = "0 0 > if 1 else 0 then"  # Should execute the 'else' part and return 0
        result = self.interpreter.run(program)
        self.assertEqual(result, 0.0)  # Expecting to return 0.0 for false condition

    def test_if_negative(self):
        program = "-5 0 > if 1 else 0 then"  # Should execute the 'else' part and return 0
        result = self.interpreter.run(program)
        self.assertEqual(result, 0.0)  # Expecting to return 0.0 for false condition

    def test_unknown_command(self):
        with self.assertRaises(ValueError):
            self.interpreter.run("unknown_command")

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestForthInterpreter))

