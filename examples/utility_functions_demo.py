"""
Utility Functions Demo

This example demonstrates various utility functions from codes_for_fun module:
- Mathematical operations
- String manipulation
- BMI calculations
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import codes_for_fun


def demonstrate_math_functions():
    """Demonstrate mathematical operations"""
    print("\n" + "="*70)
    print("MATHEMATICAL OPERATIONS")
    print("="*70)
    
    print("\n1. Factorial Calculations:")
    for n in [0, 1, 5, 10]:
        result = codes_for_fun.factorial(n)
        print(f"   factorial({n}) = {result}")
    
    print("\n2. Fibonacci Sequence:")
    fib_10 = codes_for_fun.fibonacci(10)
    print(f"   First 10 Fibonacci numbers: {fib_10}")
    
    print("\n3. Prime Number Checking:")
    test_numbers = [2, 7, 15, 17, 20, 23, 100]
    for num in test_numbers:
        is_prime = codes_for_fun.is_prime(num)
        status = "PRIME" if is_prime else "NOT PRIME"
        print(f"   {num} is {status}")
    
    print("\n4. Greatest Common Divisor:")
    pairs = [(48, 18), (100, 50), (17, 19), (54, 24)]
    for a, b in pairs:
        gcd = codes_for_fun.greatest_common_divisor(a, b)
        print(f"   GCD({a}, {b}) = {gcd}")
    
    print("\n5. Power Calculations:")
    power_examples = [(2, 3), (5, 2), (10, 0), (3, 4)]
    for base, exp in power_examples:
        result = codes_for_fun.power(base, exp)
        print(f"   {base}^{exp} = {result}")


def demonstrate_string_functions():
    """Demonstrate string manipulation"""
    print("\n" + "="*70)
    print("STRING MANIPULATION")
    print("="*70)
    
    test_string = "Hello Python World"
    
    print(f"\nOriginal string: '{test_string}'")
    print(f"1. Reversed: '{codes_for_fun.reverse_string(test_string)}'")
    print(f"2. Uppercase: '{codes_for_fun.to_uppercase(test_string)}'")
    print(f"3. Lowercase: '{codes_for_fun.to_lowercase(test_string)}'")
    print(f"4. Vowel count: {codes_for_fun.count_vowels(test_string)}")
    print(f"5. Word count: {codes_for_fun.count_words(test_string)}")
    
    print("\n6. Palindrome Checking:")
    palindromes = ["racecar", "A man a plan a canal Panama", "hello", "madam"]
    for word in palindromes:
        is_pal = codes_for_fun.is_palindrome(word)
        status = "✓ IS" if is_pal else "✗ NOT"
        print(f"   '{word}' {status} a palindrome")
    
    print("\n7. Remove Duplicates:")
    duplicate_strings = ["hello", "programming", "mississippi", "aabbcc"]
    for s in duplicate_strings:
        result = codes_for_fun.remove_duplicates(s)
        print(f"   '{s}' → '{result}'")


def demonstrate_bmi_calculator():
    """Demonstrate BMI calculations"""
    print("\n" + "="*70)
    print("BMI CALCULATOR")
    print("="*70)
    
    people = [
        {"name": "Alice", "weight": 70, "height": 175},
        {"name": "Bob", "weight": 85, "height": 180},
        {"name": "Charlie", "weight": 60, "height": 165},
        {"name": "Diana", "weight": 55, "height": 160},
    ]
    
    print("\nCalculating BMI for sample individuals:")
    print("-" * 70)
    
    for person in people:
        bmi = codes_for_fun.calculate_bmi(person["weight"], person["height"])
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        print(f"{person['name']:10} - Weight: {person['weight']}kg, "
              f"Height: {person['height']}cm")
        print(f"           BMI: {bmi:.2f} ({category})")
        print()


def demonstrate_account_generation():
    """Demonstrate account and password generation"""
    print("\n" + "="*70)
    print("ACCOUNT & PASSWORD GENERATION")
    print("="*70)
    
    users = [
        ("Julie", "Blevins"),
        ("Reiko", "Matsuki"),
        ("John", "Smith"),
        ("Emma", "Watson"),
    ]
    
    print("\nGenerating accounts for users:")
    print("-" * 70)
    
    for first, last in users:
        account = codes_for_fun.account_generator(first, last)
        password = codes_for_fun.password_generator(first, last)
        
        print(f"Name: {first} {last}")
        print(f"  Account: {account}")
        print(f"  Temp Password: {password}")
        print()


def demonstrate_character_counting():
    """Demonstrate character counting"""
    print("\n" + "="*70)
    print("CHARACTER COUNTING")
    print("="*70)
    
    text_samples = [
        ("Hello World", "l"),
        ("Mississippi", "s"),
        ("Python Programming", "p"),
        ("abracadabra", "a"),
    ]
    
    print("\nCounting specific characters in text:")
    print("-" * 70)
    
    for text, char in text_samples:
        count = codes_for_fun.count_character(text, char)
        print(f"'{text}' contains '{char}' {count} time(s)")


def main():
    """Run all demonstrations"""
    print("="*70)
    print("UTILITY FUNCTIONS - COMPREHENSIVE DEMONSTRATION")
    print("="*70)
    
    demonstrate_math_functions()
    demonstrate_string_functions()
    demonstrate_bmi_calculator()
    demonstrate_account_generation()
    demonstrate_character_counting()
    
    print("\n" + "="*70)
    print("END OF DEMONSTRATION")
    print("="*70)


if __name__ == "__main__":
    main()
