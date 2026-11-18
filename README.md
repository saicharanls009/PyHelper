# PyHelper – Python Utility Library

**Version:** 1.0.0  
**Language:** Python  
**License:** MIT

## 1. Introduction

PyHelper is a custom Python utility library developed to simplify common programming tasks. It provides reusable functions for mathematical calculations, string manipulation, security operations, file handling and date management.

The main objective of PyHelper is to reduce repetitive code and provide developers with simple, reusable and organized utility functions.

## 2. Features

PyHelper contains five independent utility modules:

### 1. Math Utilities (`math_utils.py`)
- Percentage calculation
- Factorial calculation
- Prime number checking
- Average calculation
- GCD calculation
- LCM calculation

### 2. String Utilities (`string_utils.py`)
- Reverse text
- Check palindrome
- Count words
- Count vowels
- Capitalize text
- Remove spaces

### 3. Security Utilities (`security_utils.py`)
- Generate random passwords
- Check password strength
- Generate SHA-256 hashes
- Verify hashes

### 4. File Utilities (`file_utils.py`)
- Create and write files
- Read file contents
- Copy files
- Get file extensions
- Calculate file size
- Count lines

### 5. Date Utilities (`date_utils.py`)
- Calculate age
- Calculate days between dates
- Check leap years
- Format dates
- Get current date
- Calculate days until a target date
- Find weekdays

## 3. Project Structure

```text
PyHelper/
│
├── pyhelper/
│   ├── __init__.py
│   ├── math_utils.py
│   ├── string_utils.py
│   ├── security_utils.py
│   ├── file_utils.py
│   └── date_utils.py
│
├── tests/
│   └── test_library.py
│
├── examples/
│   └── demo.py
│
├── pyproject.toml
├── README.md
└── .gitignore
```

## 4. Installation

Clone the project or download its source code.

Navigate to the project directory:

```bash
cd PyHelper
```

Create and activate a virtual environment if required:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the library:

```bash
python3 -m pip install -e .
```

## 5. Usage

Import PyHelper into your Python program.

### Example 1: Mathematical Operations

```python
from pyhelper.math_utils import factorial, is_prime

print(factorial(5))
print(is_prime(7))
```

Output:

```text
120
True
```

### Example 2: String Operations

```python
from pyhelper.string_utils import reverse_text, is_palindrome

print(reverse_text("Python"))
print(is_palindrome("madam"))
```

Output:

```text
nohtyP
True
```

### Example 3: Date Operations

```python
from pyhelper.date_utils import is_leap_year, get_weekday

print(is_leap_year(2024))
print(get_weekday("2026-11-18"))
```

Output:

```text
True
Wednesday
```

## 6. Running Examples

Run the demonstration program from the project root:

```bash
python3 -m examples.demo
```

## 7. Running Unit Tests

PyHelper uses Python's built-in `unittest` framework.

Execute:

```bash
python3 -m unittest discover -s tests -v
```

**Current testing result:**
- Total test cases: 10
- Passed: 10
- Failed: 0

## 8. Technologies Used

- Python 3
- Visual Studio Code
- Python Standard Library
- unittest Framework
- setuptools
- Git and GitHub

## 9. Future Enhancements

- Add more mathematical operations.
- Introduce data validation utilities.
- Add JSON and CSV file utilities.
- Improve security utilities.
- Expand automated test coverage.
- Publish the package on PyPI.

## 10. License

This project is licensed under the MIT License.

## 11. Conclusion

PyHelper demonstrates how a developer can design, develop, organize, test and package a reusable Python library.

It combines multiple utility modules into one structured package and provides a foundation for future improvements and additional functionality.

**Project: PyHelper – Python Utility Library**