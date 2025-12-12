"""
Codes For Fun - A Collection of Python Functions and Demonstrations

This module contains various Python functions demonstrating:
- Mathematical operations and calculations
- String manipulation techniques
- BMI calculations and health metrics
- Account and password generation
- Advanced string processing
- Loop demonstrations
"""

import datetime

# Note: random module not currently used in module functions

# ============================================================================
# MATHEMATICAL OPERATIONS
# ============================================================================


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight (float): Weight in kilograms
        height (float): Height in centimeters

    Returns:
        float: BMI value
    """
    return weight / (height / 100) ** 2


def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): Non-negative integer

    Returns:
        int: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms to generate

    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def greatest_common_divisor(a, b):
    """
    Calculate the greatest common divisor of two numbers using Euclidean algorithm.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.

    Args:
        base (float): Base number
        exponent (int): Exponent value

    Returns:
        float: Result of base^exponent
    """
    return base**exponent


# ============================================================================
# STRING MANIPULATION FUNCTIONS
# ============================================================================


def reverse_string(s):
    """
    Reverse a given string.

    Args:
        s (str): String to reverse

    Returns:
        str: Reversed string
    """
    return s[::-1]


def to_uppercase(s):
    """
    Convert a string to uppercase.

    Args:
        s (str): String to convert

    Returns:
        str: Uppercase string
    """
    return s.upper()


def to_lowercase(s):
    """
    Convert a string to lowercase.

    Args:
        s (str): String to convert

    Returns:
        str: Lowercase string
    """
    return s.lower()


def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
        s (str): String to analyze

    Returns:
        int: Number of vowels
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_palindrome(s):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).

    Args:
        s (str): String to check

    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(s):
    """
    Count the number of words in a string.

    Args:
        s (str): String to analyze

    Returns:
        int: Number of words
    """
    return len(s.split())


def remove_duplicates(s):
    """
    Remove duplicate characters from a string while preserving order.

    Args:
        s (str): String to process

    Returns:
        str: String with duplicates removed
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


# ============================================================================
# ACCOUNT AND PASSWORD GENERATION
# ============================================================================


def account_generator(first_name, last_name):
    """
    Generate an account name from first and last name.

    Args:
        first_name (str): User's first name
        last_name (str): User's last name

    Returns:
        str: Generated account name (first 3 chars of each name)
    """
    account_name = first_name[:3] + last_name[:3]
    return account_name


def password_generator(first_name, last_name):
    """
    Generate a temporary password from first and last name.

    Args:
        first_name (str): User's first name
        last_name (str): User's last name

    Returns:
        str: Generated temporary password (last 3 chars of each name)
    """
    temp_password = first_name[len(first_name) - 3 :] + last_name[len(last_name) - 3 :]
    return temp_password


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def print_each_letter(word):
    """
    Print each letter of a word on a separate line.

    Args:
        word (str): Word to print
    """
    for letter in word:
        print(letter)


def count_character(text, character):
    """
    Count occurrences of a specific character in text.

    Args:
        text (str): Text to search in
        character (str): Character to count

    Returns:
        int: Number of occurrences
    """
    counter = 0
    for char in text:
        if char == character:
            counter += 1
    return counter


def get_current_datetime():
    """
    Get the current date and time.

    Returns:
        datetime: Current datetime object
    """
    return datetime.datetime.now()


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================


def main():
    """Entry point demonstrating various functions"""
    print("=" * 70)
    print("CODES FOR FUN - FUNCTION DEMONSTRATIONS")
    print("=" * 70)

    # BMI Calculation Demo

    # BMI Calculation Demo
    print("\n" + "-" * 70)
    print("BMI CALCULATION")
    print("-" * 70)
    name = "Levi"
    height = 180.34  # height in centimeters
    weight = 86  # weight in kilograms
    bmi = calculate_bmi(weight, height)
    print(f"Calculating BMI for {name}...")
    print(f"Height: {height} cm, Weight: {weight} kg")
    print(f"BMI: {bmi:.2f}")

    # Additional personal information
    additional_info_AGE = 35
    FOOD_PREFERENCE = "TACOS"
    FAVORITE_PLACE = "MEXICO"
    LIST_OF_HOBBIES = ["GUITAR", "EATING", "IDK", "SLEEPING"]

    print(f"\nPersonal Information for {name}:")
    print(f"  Age: {additional_info_AGE}")
    print(f"  Food Preference: {FOOD_PREFERENCE}")
    print(f"  Favorite Place: {FAVORITE_PLACE}")
    print(f"  Hobbies: {', '.join(LIST_OF_HOBBIES)}")

    # Mathematical Operations Demo
    print("\n" + "-" * 70)
    print("MATHEMATICAL OPERATIONS")
    print("-" * 70)

    print(f"Factorial of 5: {factorial(5)}")
    print(f"Fibonacci sequence (10 terms): {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 20 prime? {is_prime(20)}")
    print(f"GCD of 48 and 18: {greatest_common_divisor(48, 18)}")
    print(f"2 to the power of 10: {power(2, 10)}")

    # String Manipulation Demo
    print("\n" + "-" * 70)
    print("STRING MANIPULATION")
    print("-" * 70)

    string_manipulation = "Hello, Python World!"
    print(f"Original string: {string_manipulation}")
    print(f"Reversed: {reverse_string(string_manipulation)}")
    print(f"Uppercase: {to_uppercase(string_manipulation)}")
    print(f"Lowercase: {to_lowercase(string_manipulation)}")
    print(f"Number of vowels: {count_vowels(string_manipulation)}")
    print(f"Number of words: {count_words(string_manipulation)}")

    # Palindrome check
    test_palindrome = "A man a plan a canal Panama"
    print(f"\nIs '{test_palindrome}' a palindrome? {is_palindrome(test_palindrome)}")

    # Remove duplicates demo
    duplicate_string = "programming"
    print(f"Remove duplicates from '{duplicate_string}': {remove_duplicates(duplicate_string)}")

    # Account Generation Demo
    print("\n" + "-" * 70)
    print("ACCOUNT AND PASSWORD GENERATION")
    print("-" * 70)

    first_name = "Julie"
    last_name = "Blevins"
    new_account = account_generator(first_name, last_name)
    print(f"Account for {first_name} {last_name}: {new_account}")

    first_name2 = "Reiko"
    last_name2 = "Matsuki"
    temp_password = password_generator(first_name2, last_name2)
    print(f"Temp password for {first_name2} {last_name2}: {temp_password}")

    # String Slicing Demo
    print("\n" + "-" * 70)
    print("STRING SLICING AND MANIPULATION")
    print("-" * 70)

    company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
    second_to_last = company_motto[-2]
    final_word = company_motto[-4:]
    print(f"Company motto: {company_motto}")
    print(f"Second to last character: '{second_to_last}'")
    print(f"Last 4 characters: '{final_word}'")

    # Name fixing demo
    first_name_wrong = "Bob"
    last_name_wrong = "Daily"
    fixed_first_name = "R" + first_name_wrong[1:]
    fixed_last_name = "b" + last_name_wrong[1:]
    print(f"\nFixed first name: {first_name_wrong} -> {fixed_first_name}")
    print(f"Fixed last name: {last_name_wrong} -> {fixed_last_name}")

    # Special characters
    password_with_quotes = 'theycallme"crazy"'
    print(f"Password with quotes: {password_with_quotes}")

    # Character iteration demo
    print("\n" + "-" * 70)
    print("CHARACTER ITERATION")
    print("-" * 70)
    favorite_color = "blue"
    print(f"Printing each letter of '{favorite_color}':")
    print_each_letter(favorite_color)

    # Character counting
    favorite_fruit = "blueberry"
    b_count = count_character(favorite_fruit, "b")
    print(f"\nNumber of 'b' characters in '{favorite_fruit}': {b_count}")

    # Nested list iteration
    print("\n" + "-" * 70)
    print("NESTED LIST ITERATION")
    print("-" * 70)
    groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]
    print("Original groups:")
    for group in groups:
        print(f"  {group}")

    # Modify and display
    groups[0][0] = "Levi"
    print("\nAfter modifying first element:")
    for group in groups:
        for name in group:
            print(f"  {name}")

    # Conditional statements demo
    print("\n" + "-" * 70)
    print("CONDITIONAL STATEMENTS")
    print("-" * 70)
    pet_type = "fish"
    print(f"Pet type: {pet_type}")

    if pet_type == "dog":
        print("You have a dog.")
    elif pet_type == "cat":
        print("You have a cat.")
    elif pet_type == "fish":
        print("You have a fish")
    else:
        print("Not sure!")

    # String joining demo
    print("\n" + "-" * 70)
    print("STRING OPERATIONS")
    print("-" * 70)
    x = " ".join([" Codecademy  ", " is ", " awesome "])
    print(f"Joined string: '{x}'")

    # Membership testing
    game = "Popular Nintendo Game: Mario Kart"
    print(f"\nGame title: {game}")
    print(f"Is 'l' in game title? {'l' in game}")
    print(f"Is 'x' in game title? {'x' in game}")

    # Date and time
    print("\n" + "-" * 70)
    print("DATE AND TIME")
    print("-" * 70)
    now = get_current_datetime()
    print(f"Current date and time: {now}")

    # Line joining demo
    reapers_line_one_words = [
        "Black",
        "reapers",
        "with",
        "the",
        "sound",
        "of",
        "steel",
        "on",
        "stones",
    ]
    reapers_line_one = " ".join(reapers_line_one_words)
    print(f"\nJoined words: {reapers_line_one}")

    print("\n" + "=" * 70)
    print("END OF DEMONSTRATIONS")
    print("=" * 70)


if __name__ == "__main__":
    main()
