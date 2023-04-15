import unittest
from Palindrome import palindrome
class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        resultado = palindrome('ala')
        self.assertEqual(resultado, True)
    def test_palindrome_medio(self):
        resultado = palindrome('neuquen')
        self.assertEqual(resultado, True)
    def test_palindrome_erroneo(self):
        resultado = palindrome('argentina')
        self.assertEqual(resultado, False)
    def test_palabraIronica(self):
        resultado = palindrome('aibofobia')
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()