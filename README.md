# Number Analyzer

## Overview

**Number Analyzer** is a Python 3.10 application that analyzes numbers within a specified range and categorizes them based on predefined and custom rules. The application is configurable via a JSON file, allowing for flexible and dynamic categorization.

## Features

- **Predefined Categories**: Even, Odd, Prime.
- **Custom Categories**: Define your own rules using lambda expressions in a JSON configuration file.
- **Modular Design**: Clean codebase adhering to Python best practices.
- **Command-Line Interface**: Easy interaction via the terminal.
- **Extensibility**: Easily add new categories or modify existing ones.

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

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/number-analyzer.git
   cd number-analyzer
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application uses a JSON configuration file named `analyzer-config.json` located at the root of the project. This file defines the categories and rules for number analysis.

### **Sample `analyzer-config.json`**

```json
{
  "categories": [
    {
      "label": "Even",
      "rule": "even"
    },
    {
      "label": "Prime",
      "rule": "prime"
    },
    {
      "label": "DivBy3",
      "rule": "lambda x: x % 3 == 0"
    },
    {
      "label": "Odd",
      "rule": "odd"
    },
    {
      "label": "DivBy7",
      "rule": "lambda x: x % 7 == 0"
    },
    {
      "label": "Non-Prime",
      "rule": "lambda x: x > 1 and not all(x % i != 0 for i in range(2, int(x**0.5) + 1))"
    }
  ]
}
```

- **Predefined Rules**: `"even"`, `"odd"`, `"prime"`
- **Custom Rules**: Lambda expressions as strings, e.g., `"lambda x: x % 3 == 0"`

## Usage

Run the application using the `main.py` script inside the `analyzer` package.

### **Basic Command**

```bash
python -m analyzer.main <min> <max>
```

- `<min>`: Minimum number in the range (inclusive)
- `<max>`: Maximum number in the range (inclusive)

### **Example**

Analyze numbers from 10 to 15:

```bash
python -m analyzer.main 10 15
```

### **Sample Output**

```
10: Even
11: Prime, Odd
12: Even, DivBy3
13: Prime, Odd
14: Even, DivBy7
15: DivBy3, Odd
```

## Examples

### **Analyzing a Different Range**

```bash
python -m analyzer.main 1 5
```

**Output:**

```
1: Non-Prime, Odd
2: Even, Prime
3: Prime, DivBy3, Odd
4: Even, Non-Prime
5: Prime, Odd
```

### **Using Custom Categories**

Modify `analyzer-config.json` to include a new category:

```json
{
  "label": "Square",
  "rule": "lambda x: int(x**0.5) ** 2 == x"
}
```

Now, numbers that are perfect squares will be labeled as "Square".

## Running Tests

The project includes unit tests to ensure each component functions correctly.

1. **Install Test Dependencies**

   (Already included in `requirements.txt` if using `pytest`)

2. **Run Tests**

   ```bash
   pytest
   ```

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
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

### **Steps to Contribute**

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes**

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: Replace `yourusername` with your actual GitHub username in the installation instructions.

---

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