# API Reference

Complete reference for all modules, classes, and functions in the Python Code Collection.

---

## Poets Module (`src.poets`)

Poetry management system for parsing, searching, and managing poem collections.

### Functions

#### `parse_poems(poem_string)`

Parse a comma-separated string of poems into structured data.

**Parameters:**
- `poem_string` (str): String containing poems in format "Title:Poet:Year,Title:Poet:Year,..."

**Returns:**
- `tuple`: Three lists containing (titles, poets, dates)

**Example:**
```python
poem_data = "Afterimages:Audre Lorde:1997, The Shadow:William Carlos Williams:1915"
titles, poets, dates = parse_poems(poem_data)
```

---

#### `search_by_poet(poet_name, titles, poets, dates)`

Search for all poems by a specific poet.

**Parameters:**
- `poet_name` (str): The name of the poet to search for (case-insensitive)
- `titles` (list): List of poem titles
- `poets` (list): List of poets
- `dates` (list): List of publication dates

**Returns:**
- `list`: List of tuples containing (title, poet, date) for matching poems

**Example:**
```python
results = search_by_poet("Langston Hughes", titles, poets, dates)
for title, poet, date in results:
    print(f"{title} by {poet} ({date})")
```

---

#### `display_poems_by_year(year, titles, poets, dates)`

Display all poems published in a specific year.

**Parameters:**
- `year` (str): The year to filter by
- `titles` (list): List of poem titles
- `poets` (list): List of poets
- `dates` (list): List of publication dates

**Returns:**
- `list`: List of tuples containing (title, poet, date) for poems from that year

**Example:**
```python
poems_1925 = display_poems_by_year("1925", titles, poets, dates)
```

---

#### `get_poems_by_year_range(start_year, end_year, titles, poets, dates)`

Get all poems published within a specific year range.

**Parameters:**
- `start_year` (int): Starting year (inclusive)
- `end_year` (int): Ending year (inclusive)
- `titles` (list): List of poem titles
- `poets` (list): List of poets
- `dates` (list): List of publication dates

**Returns:**
- `list`: List of tuples containing (title, poet, date) for poems in the range

**Example:**
```python
poems_1920s = get_poems_by_year_range(1920, 1930, titles, poets, dates)
```

---

#### `add_new_poem(title, poet, year, titles, poets, dates)`

Add a new poem to the dataset.

**Parameters:**
- `title` (str): Title of the new poem
- `poet` (str): Name of the poet
- `year` (str): Year of publication
- `titles` (list): List of poem titles (modified in place)
- `poets` (list): List of poets (modified in place)
- `dates` (list): List of publication dates (modified in place)

**Returns:**
- `bool`: True if poem was added successfully

**Example:**
```python
add_new_poem("The Road Not Taken", "Robert Frost", "1916", titles, poets, dates)
```

---

#### `display_all_poems(titles, poets, dates)`

Display all poems in a formatted manner.

**Parameters:**
- `titles` (list): List of poem titles
- `poets` (list): List of poets
- `dates` (list): List of publication dates

**Returns:**
- None (prints to console)

---

## Codes For Fun Module (`src.codes_for_fun`)

Collection of utility functions for mathematical operations, string manipulation, and more.

### Mathematical Operations

#### `calculate_bmi(weight, height)`

Calculate Body Mass Index (BMI).

**Parameters:**
- `weight` (float): Weight in kilograms
- `height` (float): Height in centimeters

**Returns:**
- `float`: BMI value

**Example:**
```python
bmi = calculate_bmi(70, 175)  # BMI: 22.86
```

---

#### `factorial(n)`

Calculate the factorial of a number.

**Parameters:**
- `n` (int): Non-negative integer

**Returns:**
- `int`: Factorial of n

**Example:**
```python
result = factorial(5)  # Returns 120
```

---

#### `fibonacci(n)`

Generate Fibonacci sequence up to n terms.

**Parameters:**
- `n` (int): Number of terms to generate

**Returns:**
- `list`: List of Fibonacci numbers

**Example:**
```python
fib = fibonacci(10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

#### `is_prime(n)`

Check if a number is prime.

**Parameters:**
- `n` (int): Number to check

**Returns:**
- `bool`: True if prime, False otherwise

**Example:**
```python
is_prime(17)  # True
is_prime(20)  # False
```

---

#### `greatest_common_divisor(a, b)`

Calculate the greatest common divisor using Euclidean algorithm.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- `int`: Greatest common divisor

**Example:**
```python
gcd = greatest_common_divisor(48, 18)  # Returns 6
```

---

#### `power(base, exponent)`

Calculate base raised to the power of exponent.

**Parameters:**
- `base` (float): Base number
- `exponent` (int): Exponent value

**Returns:**
- `float`: Result of base^exponent

**Example:**
```python
result = power(2, 10)  # Returns 1024
```

---

### String Manipulation

#### `reverse_string(s)`

Reverse a given string.

**Parameters:**
- `s` (str): String to reverse

**Returns:**
- `str`: Reversed string

**Example:**
```python
reverse_string("hello")  # Returns "olleh"
```

---

#### `to_uppercase(s)` / `to_lowercase(s)`

Convert string to uppercase or lowercase.

**Parameters:**
- `s` (str): String to convert

**Returns:**
- `str`: Converted string

---

#### `count_vowels(s)`

Count the number of vowels in a string.

**Parameters:**
- `s` (str): String to analyze

**Returns:**
- `int`: Number of vowels

**Example:**
```python
count_vowels("hello")  # Returns 2
```

---

#### `is_palindrome(s)`

Check if a string is a palindrome.

**Parameters:**
- `s` (str): String to check

**Returns:**
- `bool`: True if palindrome, False otherwise

**Example:**
```python
is_palindrome("racecar")  # True
is_palindrome("hello")    # False
```

---

#### `count_words(s)`

Count the number of words in a string.

**Parameters:**
- `s` (str): String to analyze

**Returns:**
- `int`: Number of words

---

#### `remove_duplicates(s)`

Remove duplicate characters while preserving order.

**Parameters:**
- `s` (str): String to process

**Returns:**
- `str`: String with duplicates removed

**Example:**
```python
remove_duplicates("hello")  # Returns "helo"
```

---

### Utilities

#### `account_generator(first_name, last_name)`

Generate an account name from first and last name.

**Parameters:**
- `first_name` (str): User's first name
- `last_name` (str): User's last name

**Returns:**
- `str`: Generated account name (first 3 chars of each name)

---

#### `password_generator(first_name, last_name)`

Generate a temporary password from first and last name.

**Parameters:**
- `first_name` (str): User's first name
- `last_name` (str): User's last name

**Returns:**
- `str`: Generated temporary password (last 3 chars of each name)

---

#### `count_character(text, character)`

Count occurrences of a specific character in text.

**Parameters:**
- `text` (str): Text to search in
- `character` (str): Character to count

**Returns:**
- `int`: Number of occurrences

---

## Random Range Module (`src.random_range`)

Random number generation and visualization toolkit.

### Functions

#### `generate_random_numbers(count, min_value, max_value, use_sample=False)`

Generate random numbers within a specified range.

**Parameters:**
- `count` (int): Number of random numbers to generate
- `min_value` (int): Minimum value (inclusive)
- `max_value` (int): Maximum value (inclusive)
- `use_sample` (bool): If True, generate unique values (no duplicates)

**Returns:**
- `list`: List of random numbers

**Example:**
```python
numbers = generate_random_numbers(10, 1, 100)
unique_numbers = generate_random_numbers(10, 1, 50, use_sample=True)
```

---

#### `calculate_statistics(numbers)`

Calculate statistical measures for a list of numbers.

**Parameters:**
- `numbers` (list): List of numbers

**Returns:**
- `dict`: Dictionary with keys: 'count', 'min', 'max', 'mean', 'range'

**Example:**
```python
numbers = [1, 2, 3, 4, 5]
stats = calculate_statistics(numbers)
# Returns: {'count': 5, 'min': 1, 'max': 5, 'mean': 3.0, 'range': 4}
```

---

#### `plot_data(x_values, y_values, plot_type='line', title=None, xlabel="Index", ylabel="Random Value")`

Plot data using specified plot type.

**Parameters:**
- `x_values` (list): X-axis values
- `y_values` (list): Y-axis values
- `plot_type` (str): Type of plot ('line', 'bar', or 'scatter')
- `title` (str): Plot title (auto-generated if None)
- `xlabel` (str): X-axis label
- `ylabel` (str): Y-axis label

**Example:**
```python
x = list(range(1, 11))
y = generate_random_numbers(10, 1, 100)
plot_data(x, y, 'line', title="My Random Data")
```

---

#### `display_statistics(stats)`

Display statistical information in a formatted manner.

**Parameters:**
- `stats` (dict): Dictionary containing statistical measures

**Returns:**
- None (prints to console)

---

#### `display_data_preview(x_values, y_values, preview_count=10)`

Display a preview of the generated data.

**Parameters:**
- `x_values` (list): X-axis values
- `y_values` (list): Y-axis values
- `preview_count` (int): Number of data points to preview

**Returns:**
- None (prints to console)

---

## Constants and Globals

### Poets Module
- `highlighted_poems`: Pre-defined string of sample poems

### Random Range Module
- `MATPLOTLIB_AVAILABLE`: Boolean indicating if matplotlib is installed
- `SEABORN_AVAILABLE`: Boolean indicating if seaborn theme is available

---

## Error Handling

All functions include basic error handling for common issues:
- Empty input strings
- Invalid data types
- Out-of-range values
- Missing dependencies (matplotlib)

For matplotlib-dependent functions, missing library is handled gracefully with informative messages.

---

## Type Hints

While the current version uses docstring type annotations, future versions may include full Python type hints for better IDE support.

---

**For more examples and usage patterns, see the [Examples Guide](examples_guide.md).**
