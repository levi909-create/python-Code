# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-12

### Added
- Initial release of Python Code Collection
- Poetry management system (`src/poets.py`)
  - Parse poem data from formatted strings
  - Search poems by poet name
  - Filter poems by year or year range
  - Add new poems to collection
  - Display formatted poem collections
  
- Utility functions collection (`src/codes_for_fun.py`)
  - Mathematical operations: factorial, fibonacci, prime checking, GCD, power
  - String manipulation: reverse, case conversion, palindrome checking, vowel counting
  - BMI calculator
  - Account and password generators
  - Character counting and text analysis
  
- Random number visualization tool (`src/random_range.py`)
  - Generate random numbers with customizable ranges
  - Support for unique samples and duplicates
  - Statistical analysis (min, max, mean, range)
  - Multiple plot types (line, bar, scatter)
  - Matplotlib-based visualizations

### Documentation
- Comprehensive README.md with badges, installation instructions, and usage examples
- CONTRIBUTING.md with detailed contribution guidelines
- MIT LICENSE file
- Complete docstrings for all functions following PEP 257
- Code organized following PEP 8 standards

### Infrastructure
- Structured directory layout (src/, tests/, examples/, docs/)
- requirements.txt for production dependencies
- requirements-dev.txt for development dependencies
- pytest testing framework setup
- GitHub Actions CI/CD pipeline
- Test coverage reporting

### Examples
- Poetry management demonstrations
- Utility function examples
- Visualization examples

---

## [Unreleased]

### Planned
- Additional mathematical functions (statistics, trigonometry)
- More data visualization options
- Interactive CLI interface
- Configuration file support
- Extended test coverage
- Performance optimizations

---

## Version History

### Version Numbering
- **Major version (X.0.0)**: Incompatible API changes
- **Minor version (0.X.0)**: Backwards-compatible new features
- **Patch version (0.0.X)**: Backwards-compatible bug fixes

### Categories
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Vulnerability fixes

[1.0.0]: https://github.com/levi909-create/python-Code/releases/tag/v1.0.0
[Unreleased]: https://github.com/levi909-create/python-Code/compare/v1.0.0...HEAD
