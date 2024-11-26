# Number Analyzer

A flexible Python tool for analyzing numbers within ranges based on configurable categories.

## Features

- Analyze numbers based on multiple categories:
  - Predefined categories (even, odd, prime)
  - Custom categories using lambda expressions
- Full support for Python's integer range capabilities:
  - 32-bit systems: approximately ±2³¹ (±2.1 billion)
  - 64-bit systems: approximately ±2⁶³ (±9.2 quintillion)
- Smart range handling:
  - Practical limit of 1 million numbers for performance
  - Warning for ranges over 500 numbers
  - Option to save large outputs to RTF files
- Beautiful output formatting:
  - Thousand separators for better readability (e.g., "1,234,567")
  - RTF file output with Courier New font
  - Clear error messages and warnings

## Installation

```bash
git clone https://github.com/yourusername/number-analyzer.git
cd number-analyzer
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Analyze numbers from 1 to 100 (prints to console)
python -m analyzer.main 1 100

# Save analysis to specific file
python -m analyzer.main 1 1000 -o results.rtf

# Save analysis with custom file name
python -m analyzer.main 1 1000 -o range_1_to_100.rtf # Custom file name

# Save analysis to custom directory
python -m analyzer.main 1 1000 -o custom_dir/results.rtf
```

By default, files are saved in the `output` directory if no path is specified. You can also specify a custom path in the `-o` argument.

### Sample Output

Console output:
```
1 to 100
1: Even, Non-Prime
2: Prime, Odd
3: Even, DivBy3, Non-Prime
...
98: Even, Non-Prime
99: Prime, Odd
100: Even, Non-Prime

or

Results saved to: number-analyzer/output/results.rtf
```

RTF file output includes:
- Courier New font for consistent spacing
- Numbers formatted with thousand separators
- One number per line with its categories
- Clear header showing the analyzed range

### File Organization

The analyzer automatically organizes output files in a dedicated `output` directory:

```
output/
├── range_1_to_100.rtf
├── range_1_to_100_1.rtf    # Duplicate handling
├── range_101_to_200.rtf
└── custom_name.rtf
```

#### File Naming Convention
- Default format: `range_[min]_to_[max].rtf`
- Duplicate handling: Appends counter (e.g., `range_1_to_100_1.rtf`)
- Custom names preserve extension (e.g., `custom_name_1.rtf`)

## Configuration

Create a `analyzer-config.json` file:

```json
{
  "categories": [
    {"label": "Even", "rule": "even"},
    {"label": "Odd", "rule": "odd"},
    {"label": "Prime", "rule": "prime"},
    {"label": "DivBy3", "rule": "lambda x: x % 3 == 0"}
  ]
}
```

## Limitations and Warnings

### System Limits
- Maximum range depends on your Python installation:
  - 32-bit: ±2.1 billion (±2³¹)
  - 64-bit: ±9.2 quintillion (±2⁶³)

### Practical Limits
- Maximum recommended range: 1 million numbers
- Warning threshold: 500 numbers
- Larger ranges will trigger:
  - Warning and file output option (>500 numbers)
  - Error message (>1 million numbers)

### Performance Considerations
- Prime number checking becomes slower for very large numbers
- Memory usage increases with range size
- Consider using file output for ranges >500 numbers

## Error Messages

You might encounter these messages:

```
# System limit exceeded
Error: Values must be between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807 on this system

# Practical limit exceeded
Error: Range size (1,500,000 numbers) exceeds practical limit of 1,000,000

# Large range warning
Warning: Large range detected (750 numbers). Would you like to save the output to a file? (y/n):
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- **Python 3.10** or higher
- **Git** (for cloning the repository)
- **pip** (Python package installer)

## Project Structure

```
number-analyzer/
├── analyzer/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   ├── config_loader.py
│   ├── number_analyzer.py
│   └── categories/
│       ├── __init__.py
│       ├── base_category.py
│       ├── even.py
│       ├── odd.py
│       ├── prime.py
│       └── custom.py
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_config_loader.py
│   ├── test_number_analyzer.py
│   └── test_categories/
│       ├── __init__.py
│       ├── test_even.py
│       ├── test_odd.py
│       ├── test_prime.py
│       └── test_custom.py
├── analyzer-config.json
├── requirements.txt
├── README.md
├── .gitignore
└── output/
    ├── range_1_to_100.rtf
    ├── range_1_to_100_1.rtf
    ├── range_101_to_200.rtf
    └── custom_name.rtf
```

## Running Tests

The project includes unit tests to ensure each component functions correctly.

1. **Install Test Dependencies**

   (Already included in `requirements.txt` if using `pytest`)

2. **Run Tests**

   ```bash
   pytest
   ```

## Additional Information

### **Error Handling**

- The application includes error handling to manage exceptions that may occur during the evaluation of custom rules.
- If a custom rule causes an error, the application will print an error message but continue running.

### **Security Considerations**

- **Eval Usage**: The application uses `eval` to evaluate custom lambda expressions. To mitigate security risks:
  - The `eval` function is called with a restricted scope, limiting access to built-in functions and modules.
  - Only necessary functions are made available, such as `abs` and `math`.
- **Recommendation**: Always ensure that the `analyzer-config.json` file is from a trusted source.

### **Extending the Application**

- **Adding New Predefined Categories**:
  1. Create a new Python file in `analyzer/categories/`, e.g., `perfect.py`.
  2. Define a class that extends `BaseCategory`.
  3. Implement the `matches` method with the desired logic.
  4. Import and instantiate the new category in `number_analyzer.py`.

- **Using More Complex Custom Rules**:
  - Custom rules can be as complex as needed, provided they are valid Python expressions.
  - Remember to update the allowed functions in the `CustomCategory` class if your rule requires additional functions.

### **Contact Information**

For questions or support, please open an issue on the GitHub repository or contact the maintainer at [mungb.pro@gmail.com](mailto:mungb.pro@gmail.com).