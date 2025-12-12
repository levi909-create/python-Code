# Getting Started

This guide will help you get up and running with the Python Code Collection.

## Prerequisites

Before you begin, ensure you have:
- Python 3.7 or higher installed
- pip (Python package installer)
- Git (for cloning the repository)

### Checking Your Python Version

```bash
python --version
# or
python3 --version
```

If you need to install Python, visit [python.org](https://www.python.org/downloads/).

## Installation

### Method 1: Clone and Install (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/levi909-create/python-Code.git
   cd python-Code
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **For development (includes testing tools):**
   ```bash
   pip install -r requirements-dev.txt
   ```

### Method 2: Install as Package

Install the package in development mode to use it as a library:

```bash
cd python-Code
pip install -e .
```

## Quick Start

### Running the Examples

The easiest way to see what the project can do is to run the example scripts:

```bash
# Poetry management demo
python examples/poets_demo.py

# Utility functions demo
python examples/utility_functions_demo.py

# Random number visualization demo
python examples/visualization_demo.py
```

### Using Individual Modules

#### Example 1: Poetry Management

```python
from src import poets

# Sample poem data
poem_data = "Afterimages:Audre Lorde:1997, The Shadow:William Carlos Williams:1915"

# Parse poems
titles, poets_list, dates = poets.parse_poems(poem_data)

# Search for poems
results = poets.search_by_poet("Audre Lorde", titles, poets_list, dates)
print(results)
```

#### Example 2: Utility Functions

```python
from src import codes_for_fun

# Calculate BMI
bmi = codes_for_fun.calculate_bmi(weight=70, height=175)
print(f"BMI: {bmi:.2f}")

# Generate Fibonacci sequence
fib = codes_for_fun.fibonacci(10)
print(f"Fibonacci: {fib}")

# Check if number is prime
is_prime = codes_for_fun.is_prime(17)
print(f"Is 17 prime? {is_prime}")
```

#### Example 3: Random Number Generation

```python
from src import random_range

# Generate random numbers
numbers = random_range.generate_random_numbers(10, 1, 100)
print(f"Random numbers: {numbers}")

# Calculate statistics
stats = random_range.calculate_statistics(numbers)
print(f"Statistics: {stats}")

# Visualize data (requires matplotlib)
x_values = list(range(1, 11))
random_range.plot_data(x_values, numbers, 'line')
```

## Running Tests

To verify everything is working correctly:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_poets.py -v
```

## Common Issues

### Issue: `matplotlib` not found

**Solution:** Install matplotlib for visualization features:
```bash
pip install matplotlib
```

### Issue: `ModuleNotFoundError: No module named 'src'`

**Solution:** Make sure you're running Python from the project root directory or add the project to your Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Issue: Tests fail with import errors

**Solution:** Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

## Next Steps

Now that you have the project set up:

1. **Explore the Examples** - Run through all example scripts to see what's possible
2. **Read the API Reference** - Learn about all available functions and their parameters
3. **Try Building Something** - Use the modules to create your own project
4. **Run Tests** - Understand how the code is tested
5. **Contribute** - See [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute

## Project Structure

```
python-Code/
├── src/                    # Source code
│   ├── __init__.py
│   ├── poets.py           # Poetry management
│   ├── codes_for_fun.py   # Utility functions
│   └── random_range.py    # Random number tools
├── tests/                 # Test files
│   ├── test_poets.py
│   ├── test_codes_for_fun.py
│   └── test_random_range.py
├── examples/              # Example scripts
│   ├── poets_demo.py
│   ├── utility_functions_demo.py
│   └── visualization_demo.py
├── docs/                  # Documentation
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── setup.py              # Package setup
├── pyproject.toml        # Modern Python packaging
└── README.md             # Main readme
```

## Getting Help

- **Documentation**: Check the `docs/` directory
- **Examples**: Look at the `examples/` directory
- **Issues**: [GitHub Issues](https://github.com/levi909-create/python-Code/issues)
- **Contributing**: See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

Ready to dive deeper? Check out the [API Reference](api_reference.md) next!
