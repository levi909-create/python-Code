# Development Guide

This guide provides information for developers who want to contribute to the Python Code Collection project.

## Development Setup

### 1. Prerequisites

- Python 3.7 or higher
- Git
- pip

### 2. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/levi909-create/python-Code.git
cd python-Code

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Edit files in the appropriate directories:
- `src/` - Source code
- `tests/` - Test files
- `examples/` - Example scripts
- `docs/` - Documentation

### 3. Format Your Code

```bash
# Format with black
black src/ tests/ examples/

# Check with flake8
flake8 src/ tests/ examples/ --max-line-length=127
```

### 4. Run Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_poets.py -v
```

### 5. Commit and Push

```bash
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

## Project Structure

```
python-Code/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD
├── docs/                    # Documentation
│   ├── README.md
│   ├── getting_started.md
│   ├── api_reference.md
│   └── development_guide.md
├── examples/               # Example scripts
│   ├── README.md
│   ├── poets_demo.py
│   ├── utility_functions_demo.py
│   └── visualization_demo.py
├── src/                    # Source code
│   ├── __init__.py
│   ├── poets.py           # Poetry management
│   ├── codes_for_fun.py   # Utility functions
│   └── random_range.py    # Random number tools
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_poets.py
│   ├── test_codes_for_fun.py
│   └── test_random_range.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml         # Modern Python packaging
├── requirements.txt        # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── setup.cfg              # pytest configuration
└── setup.py               # Package setup
```

## Code Standards

### Style Guidelines

- **PEP 8**: Follow Python Enhancement Proposal 8
- **Line Length**: Maximum 100 characters (configured in black)
- **Imports**: Organize imports (stdlib, third-party, local)
- **Docstrings**: Use Google-style or NumPy-style docstrings

### Documentation Requirements

Every function should have:
- Brief description
- Parameters with types
- Return value with type
- Examples (when helpful)
- Raises section (if applicable)

Example:
```python
def my_function(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: When input is invalid
    
    Example:
        >>> my_function(5, "test")
        True
    """
    pass
```

## Testing Guidelines

### Writing Tests

1. **Test Organization**: Group related tests in classes
2. **Test Names**: Use descriptive names starting with `test_`
3. **Test Coverage**: Aim for at least 80% coverage
4. **Assertions**: Use clear assertion messages

Example:
```python
class TestMyFunction:
    """Tests for my_function"""
    
    def test_basic_functionality(self):
        """Test basic usage"""
        result = my_function(5, "test")
        assert result is True, "Expected True for valid input"
    
    def test_edge_case(self):
        """Test edge case handling"""
        result = my_function(0, "")
        assert result is False, "Expected False for empty input"
```

### Running Specific Tests

```bash
# Run a specific test file
pytest tests/test_poets.py

# Run a specific test class
pytest tests/test_poets.py::TestParsePoems

# Run a specific test method
pytest tests/test_poets.py::TestParsePoems::test_parse_single_poem

# Run tests matching pattern
pytest -k "test_parse"
```

## Continuous Integration

The project uses GitHub Actions for CI/CD:

- **Tests**: Run on Python 3.7, 3.8, 3.9, 3.10, 3.11
- **Linting**: flake8 checks
- **Formatting**: black verification
- **Code Quality**: pylint analysis
- **Build**: Package build verification

CI runs automatically on:
- Push to main branch
- Pull requests to main
- Push to copilot/** branches

## Dependencies

### Production Dependencies
- `matplotlib>=3.5.0` - For visualization

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `pytest-cov>=4.0.0` - Coverage reporting
- `flake8>=6.0.0` - Style checker
- `black>=23.0.0` - Code formatter
- `pylint>=2.15.0` - Code analyzer
- `mypy>=1.0.0` - Type checker

## Adding New Features

### 1. Plan Your Feature

- Discuss in an issue first for major changes
- Review existing code to match style
- Consider backward compatibility

### 2. Implement

1. Write the feature code in `src/`
2. Add tests in `tests/`
3. Add examples in `examples/`
4. Update documentation in `docs/`
5. Update CHANGELOG.md

### 3. Test Thoroughly

```bash
# Run full test suite
pytest

# Check coverage
pytest --cov=src --cov-report=term-missing

# Format code
black src/ tests/ examples/

# Lint code
flake8 src/ tests/ examples/
```

### 4. Document

- Add/update docstrings
- Update API reference if needed
- Add usage examples
- Update README if necessary

## Debugging

### Using pytest with pdb

```bash
# Drop into debugger on failure
pytest --pdb

# Drop into debugger at start of each test
pytest --trace
```

### Verbose Output

```bash
# Very verbose output
pytest -vv

# Show print statements
pytest -s

# Show locals on failure
pytest -l
```

## Release Process

1. Update version in `setup.py` and `pyproject.toml`
2. Update `CHANGELOG.md`
3. Run full test suite
4. Create git tag: `git tag -a v1.0.0 -m "Release v1.0.0"`
5. Push tag: `git push origin v1.0.0`
6. Create GitHub release

## Getting Help

- **Issues**: GitHub Issues for bugs and features
- **Discussions**: GitHub Discussions for questions
- **Contributing**: See [CONTRIBUTING.md](../CONTRIBUTING.md)

## Common Tasks

### Run All Quality Checks

```bash
# One command to rule them all
pytest && black --check src/ tests/ examples/ && flake8 src/ tests/ examples/
```

### Update Dependencies

```bash
# Update dev dependencies
pip install --upgrade -r requirements-dev.txt

# Update production dependencies
pip install --upgrade -r requirements.txt
```

### Generate Coverage Report

```bash
# Generate HTML coverage report
pytest --cov=src --cov-report=html

# Open in browser
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## Best Practices

1. **Write Tests First**: Consider TDD approach
2. **Small Commits**: Make focused, atomic commits
3. **Clear Messages**: Write descriptive commit messages
4. **Code Review**: Request reviews for significant changes
5. **Documentation**: Keep docs up to date
6. **Backward Compatibility**: Don't break existing APIs without versioning

## Performance Considerations

- Profile code before optimizing
- Use appropriate data structures
- Consider memory usage for large datasets
- Document performance characteristics

## Security

- Never commit secrets or credentials
- Sanitize user input
- Follow security best practices
- Report security issues privately

---

**Happy Coding!** 🚀
