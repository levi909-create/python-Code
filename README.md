# Python Code Collection 🐍

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI Status](https://img.shields.io/badge/CI-passing-brightgreen.svg)](https://github.com/levi909-create/python-Code/actions)

A professional collection of Python learning projects demonstrating various programming concepts, algorithms, and utilities. This repository serves as a showcase of Python proficiency and best practices.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Examples](#examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Poetry Management System**: Parse, search, and analyze poetry data with ease
- **Utility Functions Collection**: Mathematical operations, string manipulation, and more
- **Random Number Visualization**: Generate and visualize random data with multiple plot types
- **Well-Documented Code**: Comprehensive docstrings following PEP 257 standards
- **Unit Testing**: Full test coverage with pytest
- **CI/CD Pipeline**: Automated testing with GitHub Actions

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/levi909-create/python-Code.git
   cd python-Code
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **For development (includes testing and linting tools):**
   ```bash
   pip install -r requirements-dev.txt
   ```

### Using as a Package

Install the package in development mode:
```bash
pip install -e .
```

## 📖 Usage

### Command Line Usage

Each module can be run independently:

```bash
# Run the Poetry Management System
python src/poets.py

# Run the Utility Functions demonstrations
python src/codes_for_fun.py

# Run the Random Number Visualization tool
python src/random_range.py
```

### Import as a Library

```python
# Import specific modules
from src import poets, codes_for_fun, random_range

# Use poetry functions
titles, poets_list, dates = poets.parse_poems(poem_string)
results = poets.search_by_poet("Langston Hughes", titles, poets_list, dates)

# Use utility functions
bmi = codes_for_fun.calculate_bmi(weight=70, height=175)
fib = codes_for_fun.fibonacci(10)

# Use random number generation
numbers = random_range.generate_random_numbers(count=20, min_value=1, max_value=100)
stats = random_range.calculate_statistics(numbers)
```

## 📦 Modules

### 1. Poets (`src/poets.py`)

A comprehensive poetry management system that provides:
- Parsing poem data from formatted strings
- Searching poems by poet name
- Filtering poems by year or year range
- Adding new poems to the collection
- Displaying formatted poem collections

**Key Functions:**
- `parse_poems(poem_string)` - Parse comma-separated poem data
- `search_by_poet(poet_name, titles, poets, dates)` - Find poems by poet
- `display_poems_by_year(year, titles, poets, dates)` - Filter by year
- `get_poems_by_year_range(start_year, end_year, ...)` - Filter by year range
- `add_new_poem(title, poet, year, ...)` - Add new entries

### 2. Codes For Fun (`src/codes_for_fun.py`)

A collection of utility functions demonstrating Python capabilities:

**Mathematical Operations:**
- `calculate_bmi(weight, height)` - Calculate Body Mass Index
- `factorial(n)` - Calculate factorial
- `fibonacci(n)` - Generate Fibonacci sequence
- `is_prime(n)` - Check if number is prime
- `greatest_common_divisor(a, b)` - Calculate GCD
- `power(base, exponent)` - Power calculation

**String Manipulation:**
- `reverse_string(s)` - Reverse a string
- `to_uppercase(s)` / `to_lowercase(s)` - Case conversion
- `count_vowels(s)` - Count vowels in string
- `is_palindrome(s)` - Check if palindrome
- `count_words(s)` - Count words
- `remove_duplicates(s)` - Remove duplicate characters

**Utilities:**
- `account_generator(first_name, last_name)` - Generate account names
- `password_generator(first_name, last_name)` - Generate temporary passwords
- `count_character(text, character)` - Count character occurrences

### 3. Random Range (`src/random_range.py`)

Random number generation and visualization toolkit:

**Features:**
- Generate random numbers with customizable ranges
- Support for unique samples (no duplicates) or with replacement
- Statistical analysis (min, max, mean, range)
- Multiple plot types (line, bar, scatter)
- Matplotlib-based visualizations

**Key Functions:**
- `generate_random_numbers(count, min_value, max_value, use_sample)` - Generate random numbers
- `calculate_statistics(numbers)` - Statistical analysis
- `plot_data(x_values, y_values, plot_type, ...)` - Visualize data
- `display_statistics(stats)` - Format and display statistics

## 🎯 Examples

See the [`examples/`](examples/) directory for detailed usage examples:

- `examples/poets_demo.py` - Poetry management demonstrations
- `examples/utility_functions_demo.py` - Mathematical and string operations
- `examples/visualization_demo.py` - Random number visualization examples

Run examples:
```bash
python examples/poets_demo.py
```

## 🧪 Testing

This project uses pytest for testing. Tests are located in the `tests/` directory.

### Run all tests:
```bash
pytest
```

### Run tests with coverage report:
```bash
pytest --cov=src --cov-report=html
```

### Run specific test file:
```bash
pytest tests/test_poets.py
```

### Run tests in verbose mode:
```bash
pytest -v
```

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- Code of Conduct
- Development process
- How to submit pull requests
- Coding standards and conventions

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and version updates.

## 👨‍💻 Author

**Levi**
- GitHub: [@levi909-create](https://github.com/levi909-create)

## 🙏 Acknowledgments

- Thanks to all contributors who have helped improve this project
- Inspired by various Python learning resources and best practices

---

**Made with ❤️ and Python**
