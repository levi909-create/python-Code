# Copilot Instructions for python-Code Repository

This repository contains a collection of Python learning projects and code demonstrations. Follow these guidelines when working with this codebase.

## Project Overview

This is a personal Python repository tracking progress with various Python concepts including:
- Mathematical operations and algorithms
- String manipulation and processing
- Data visualization with matplotlib
- Poetry data management and analysis
- Random number generation utilities

## Code Style and Conventions

### Python Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names in snake_case
- Keep functions focused on single responsibilities
- Maintain clear separation between different functional areas using section dividers

### Documentation Standards
- All modules must have a module-level docstring explaining:
  - Purpose of the module
  - Key functionality provided (as bullet points)
- All functions must include docstrings with:
  - Brief description of what the function does
  - Args section listing all parameters with types and descriptions
  - Returns section describing return value and type
- Use Google-style docstrings format (as seen in existing code)
- Include section dividers using comment blocks with `=` characters for major code sections

**Example:**
```python
"""
Module Name - Brief description

This module provides functionality to:
- Feature 1
- Feature 2
- Feature 3
"""

# ============================================================================
# SECTION NAME
# ============================================================================

def function_name(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
    
    Returns:
        type: Description of return value
    """
    # Implementation
    pass
```

### Code Organization
- Group related functions together under descriptive section headers
- Use clear section dividers to separate different functional areas
- Place imports at the top of the file
- Handle import errors gracefully with try/except blocks when importing optional dependencies

### Error Handling
- Provide graceful fallbacks for missing optional dependencies (like matplotlib)
- Include helpful error messages or warnings when issues occur
- Validate input parameters where appropriate

### Dependencies
- Minimize external dependencies where possible
- When external libraries are required (like matplotlib), handle their absence gracefully
- Document any required dependencies in comments or docstrings

## Testing
- This repository currently does not have a formal test suite
- When adding new functionality, ensure it can be manually tested
- Include example usage in docstrings where helpful

## File Naming
- Use lowercase with underscores for module names (snake_case)
- Choose descriptive names that indicate the module's purpose

## Best Practices for This Repository
- Maintain consistency with existing code style and documentation format
- Preserve the educational nature of the code with clear explanations
- Keep code readable and well-commented for learning purposes
- When refactoring, maintain backward compatibility with existing functions
- Add new features as clearly separated sections with appropriate documentation
