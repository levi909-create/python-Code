# Contributing to Python Code Collection

Thank you for your interest in contributing to the Python Code Collection! This document provides guidelines and instructions for contributing to this project.

## 📜 Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

- **Be Respectful**: Treat everyone with respect and kindness
- **Be Collaborative**: Work together and help others
- **Be Professional**: Maintain a professional attitude in all interactions
- **Be Open-Minded**: Welcome different perspectives and ideas

## 🚀 Getting Started

### 1. Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-Code.git
   cd python-Code
   ```

### 2. Set Up Development Environment

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

### 3. Create a Branch

Create a new branch for your feature or bugfix:
```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/add-new-function` - For new features
- `bugfix/fix-calculation-error` - For bug fixes
- `docs/update-readme` - For documentation updates
- `test/add-missing-tests` - For test additions

## 💻 Development Guidelines

### Code Style

This project follows PEP 8 style guidelines with the following specifics:

- **Line Length**: Maximum 100 characters
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Prefer double quotes for strings
- **Formatting**: Use `black` for automatic formatting

Run formatters before committing:
```bash
# Format code with black
black src/ tests/

# Check style with flake8
flake8 src/ tests/
```

### Documentation Standards

- **Module Docstrings**: Every module should have a docstring explaining its purpose
- **Function Docstrings**: All functions must have docstrings following PEP 257
- **Inline Comments**: Use sparingly, only when code intent is not clear

**Docstring Format Example:**
```python
def function_name(param1, param2):
    """
    Brief description of function purpose.
    
    Detailed explanation if necessary. Can span multiple lines
    and provide context about the function's behavior.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
    
    Returns:
        type: Description of return value
    
    Raises:
        ErrorType: Description of when this error is raised
    
    Example:
        >>> function_name(value1, value2)
        expected_output
    """
    # Implementation
```

### Testing Requirements

- **Test Coverage**: Aim for at least 80% code coverage
- **Test Organization**: Place tests in the `tests/` directory
- **Test Naming**: Use descriptive test function names starting with `test_`
- **Assertions**: Use clear assertion messages

**Test Example:**
```python
def test_calculate_bmi_normal_weight():
    """Test BMI calculation for normal weight range."""
    result = calculate_bmi(weight=70, height=175)
    assert 22.0 < result < 23.0, "BMI should be in normal range"
```

Run tests before submitting:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_poets.py -v
```

## 📝 Making Changes

### 1. Write Your Code

- Keep changes focused and atomic
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 2. Test Your Changes

```bash
# Run tests
pytest

# Check code style
flake8 src/ tests/

# Format code
black src/ tests/
```

### 3. Commit Your Changes

Write clear, concise commit messages:

```bash
git add .
git commit -m "Add function to calculate standard deviation

- Implement standard_deviation() function
- Add unit tests for edge cases
- Update documentation with usage examples"
```

**Commit Message Guidelines:**
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be a summary (50 chars or less)
- Add detailed description after a blank line if needed
- Reference issue numbers when applicable

### 4. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Detailed description of what was changed and why
- Reference to any related issues
- Screenshots (if applicable)

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Detailed steps to reproduce the issue
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Environment**: Python version, OS, relevant dependencies
6. **Code Sample**: Minimal code example demonstrating the issue

**Bug Report Template:**
```markdown
### Description
Brief description of the bug

### Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

### Expected Behavior
What should happen

### Actual Behavior
What actually happens

### Environment
- Python version: 3.9
- OS: Ubuntu 20.04
- Dependencies: matplotlib 3.5.0

### Code Sample
\```python
# Minimal reproducible example
\```
```

## 💡 Suggesting Features

Feature suggestions are welcome! Please:

1. Check if the feature has already been suggested
2. Provide a clear description of the feature
3. Explain the use case and benefits
4. Include examples of how it would work

## 📋 Pull Request Checklist

Before submitting your pull request, verify:

- [ ] Code follows PEP 8 style guidelines
- [ ] All tests pass (`pytest`)
- [ ] New code has test coverage
- [ ] Documentation is updated (README, docstrings, etc.)
- [ ] Code is formatted with `black`
- [ ] No linting errors (`flake8`)
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main branch

## 🔍 Code Review Process

1. Maintainers will review your PR
2. Feedback will be provided via PR comments
3. Make requested changes and push updates
4. Once approved, your PR will be merged

**Review Timeline:**
- Initial review: Within 3-5 days
- Feedback response: Please respond within 2 weeks

## 🎯 Areas for Contribution

Looking for ideas? Here are areas that need attention:

- **Documentation**: Improve examples and tutorials
- **Testing**: Increase test coverage
- **Features**: Add new utility functions
- **Performance**: Optimize existing algorithms
- **Bug Fixes**: Address reported issues

## 📞 Getting Help

Need help? You can:

- Open an issue for questions
- Check existing documentation
- Review closed PRs for examples

## 🙏 Recognition

Contributors will be:
- Listed in the project contributors
- Mentioned in release notes for significant contributions
- Credited in relevant documentation

Thank you for contributing to Python Code Collection! Your efforts help make this project better for everyone.

---

**Happy Coding! 🐍**
