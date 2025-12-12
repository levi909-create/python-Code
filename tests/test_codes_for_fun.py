"""
Unit tests for the codes_for_fun module.

Tests cover:
- Mathematical operations
- String manipulation
- BMI calculations
- Account and password generation
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import codes_for_fun  # noqa: E402


class TestMathematicalOperations:
    """Tests for mathematical functions"""

    def test_calculate_bmi_normal(self):
        """Test BMI calculation for normal values"""
        bmi = codes_for_fun.calculate_bmi(70, 175)
        assert 22.0 < bmi < 23.5

    def test_calculate_bmi_underweight(self):
        """Test BMI calculation for underweight"""
        bmi = codes_for_fun.calculate_bmi(50, 175)
        assert bmi < 18.5

    def test_factorial_zero(self):
        """Test factorial of 0"""
        assert codes_for_fun.factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of 1"""
        assert codes_for_fun.factorial(1) == 1

    def test_factorial_five(self):
        """Test factorial of 5"""
        assert codes_for_fun.factorial(5) == 120

    def test_factorial_ten(self):
        """Test factorial of 10"""
        assert codes_for_fun.factorial(10) == 3628800

    def test_fibonacci_zero(self):
        """Test Fibonacci with 0 terms"""
        assert codes_for_fun.fibonacci(0) == []

    def test_fibonacci_one(self):
        """Test Fibonacci with 1 term"""
        assert codes_for_fun.fibonacci(1) == [0]

    def test_fibonacci_ten(self):
        """Test Fibonacci with 10 terms"""
        result = codes_for_fun.fibonacci(10)
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_is_prime_two(self):
        """Test prime checking for 2"""
        assert codes_for_fun.is_prime(2) is True

    def test_is_prime_seventeen(self):
        """Test prime checking for 17"""
        assert codes_for_fun.is_prime(17) is True

    def test_is_prime_composite(self):
        """Test prime checking for composite numbers"""
        assert codes_for_fun.is_prime(4) is False
        assert codes_for_fun.is_prime(15) is False
        assert codes_for_fun.is_prime(20) is False

    def test_is_prime_negative(self):
        """Test prime checking for negative numbers"""
        assert codes_for_fun.is_prime(-5) is False

    def test_is_prime_zero_and_one(self):
        """Test prime checking for 0 and 1"""
        assert codes_for_fun.is_prime(0) is False
        assert codes_for_fun.is_prime(1) is False

    def test_greatest_common_divisor_basic(self):
        """Test GCD calculation"""
        assert codes_for_fun.greatest_common_divisor(48, 18) == 6
        assert codes_for_fun.greatest_common_divisor(100, 50) == 50
        assert codes_for_fun.greatest_common_divisor(17, 19) == 1

    def test_power_basic(self):
        """Test power calculation"""
        assert codes_for_fun.power(2, 3) == 8
        assert codes_for_fun.power(5, 2) == 25
        assert codes_for_fun.power(10, 0) == 1


class TestStringManipulation:
    """Tests for string manipulation functions"""

    def test_reverse_string_basic(self):
        """Test string reversal"""
        assert codes_for_fun.reverse_string("hello") == "olleh"
        assert codes_for_fun.reverse_string("Python") == "nohtyP"

    def test_reverse_string_empty(self):
        """Test reversing empty string"""
        assert codes_for_fun.reverse_string("") == ""

    def test_to_uppercase(self):
        """Test uppercase conversion"""
        assert codes_for_fun.to_uppercase("hello") == "HELLO"
        assert codes_for_fun.to_uppercase("Python") == "PYTHON"

    def test_to_lowercase(self):
        """Test lowercase conversion"""
        assert codes_for_fun.to_lowercase("HELLO") == "hello"
        assert codes_for_fun.to_lowercase("Python") == "python"

    def test_count_vowels_basic(self):
        """Test vowel counting"""
        assert codes_for_fun.count_vowels("hello") == 2
        assert codes_for_fun.count_vowels("Python") == 1
        assert codes_for_fun.count_vowels("aeiou") == 5
        assert codes_for_fun.count_vowels("AEIOU") == 5

    def test_count_vowels_no_vowels(self):
        """Test counting vowels in string with no vowels"""
        assert codes_for_fun.count_vowels("xyz") == 0

    def test_is_palindrome_true(self):
        """Test palindrome detection for valid palindromes"""
        assert codes_for_fun.is_palindrome("racecar") is True
        assert codes_for_fun.is_palindrome("A man a plan a canal Panama") is True
        assert codes_for_fun.is_palindrome("madam") is True

    def test_is_palindrome_false(self):
        """Test palindrome detection for non-palindromes"""
        assert codes_for_fun.is_palindrome("hello") is False
        assert codes_for_fun.is_palindrome("Python") is False

    def test_count_words_basic(self):
        """Test word counting"""
        assert codes_for_fun.count_words("hello world") == 2
        assert codes_for_fun.count_words("Python is great") == 3
        assert codes_for_fun.count_words("one") == 1

    def test_count_words_empty(self):
        """Test counting words in empty string"""
        assert codes_for_fun.count_words("") == 0

    def test_remove_duplicates_basic(self):
        """Test removing duplicate characters"""
        assert codes_for_fun.remove_duplicates("hello") == "helo"
        assert codes_for_fun.remove_duplicates("programming") == "progamin"

    def test_remove_duplicates_no_duplicates(self):
        """Test removing duplicates from string with no duplicates"""
        assert codes_for_fun.remove_duplicates("abc") == "abc"


class TestAccountAndPasswordGeneration:
    """Tests for account and password generation"""

    def test_account_generator_basic(self):
        """Test account name generation"""
        assert codes_for_fun.account_generator("Julie", "Blevins") == "JulBle"
        assert codes_for_fun.account_generator("John", "Doe") == "JohDoe"

    def test_account_generator_short_names(self):
        """Test account generation with names shorter than 3 chars"""
        assert codes_for_fun.account_generator("Jo", "Li") == "JoLi"
        assert codes_for_fun.account_generator("A", "B") == "AB"

    def test_password_generator_basic(self):
        """Test temporary password generation"""
        assert codes_for_fun.password_generator("Reiko", "Matsuki") == "ikouki"
        assert codes_for_fun.password_generator("Julie", "Blevins") == "lieins"

    def test_password_generator_short_names(self):
        """Test password generation with names shorter than 3 chars"""
        # For names shorter than 3 chars, it takes what's available from the end
        result = codes_for_fun.password_generator("Jo", "Li")
        assert len(result) > 0  # Should return something


class TestUtilityFunctions:
    """Tests for utility functions"""

    def test_count_character_basic(self):
        """Test character counting"""
        assert codes_for_fun.count_character("hello", "l") == 2
        assert codes_for_fun.count_character("blueberry", "b") == 2
        assert codes_for_fun.count_character("Python", "P") == 1

    def test_count_character_not_found(self):
        """Test counting character not in string"""
        assert codes_for_fun.count_character("hello", "z") == 0

    def test_get_current_datetime(self):
        """Test getting current datetime"""
        result = codes_for_fun.get_current_datetime()
        assert result is not None
        assert hasattr(result, "year")
        assert hasattr(result, "month")
        assert hasattr(result, "day")
