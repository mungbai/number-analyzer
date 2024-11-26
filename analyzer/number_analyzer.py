"""
Number Analyzer Module

This module contains the core functionality for analyzing numbers based on
configurable categories. It provides a flexible system for categorizing numbers
according to both predefined and custom rules.

Key Features:
- Support for predefined categories (even, odd, prime)
- Support for custom categories via lambda expressions
- Efficient number analysis within specified ranges
- Extensible category system
- Range validation and output options

Author: mungbai
Date: 2024
"""

import os
import sys
from datetime import datetime
from .categories import (
    Even,
    Odd,
    Prime,
    CustomCategory
)


class NumberAnalyzer:
    """
    A class that analyzes numbers based on configurable categories.
    
    This class serves as the main engine for number analysis, managing multiple
    category instances and coordinating the analysis process. It supports both
    predefined categories (even, odd, prime) and custom categories defined through
    lambda expressions.
    
    Attributes:
        categories (list[BaseCategory]): A list of category instances used for analysis
        MIN_VALUE (int): Minimum allowed value for analysis (system's min int)
        MAX_VALUE (int): Maximum allowed value for analysis (system's max int)
        RANGE_WARNING (int): Range size that triggers a warning (500)
        PRACTICAL_LIMIT (int): Practical limit for analysis (10^6, for performance)
    """
    
    # Get system's integer limits
    MIN_VALUE = -sys.maxsize - 1  # Usually -2^31 on 32-bit, -2^63 on 64-bit
    MAX_VALUE = sys.maxsize       # Usually 2^31 - 1 on 32-bit, 2^63 - 1 on 64-bit
    RANGE_WARNING = 500
    PRACTICAL_LIMIT = 1_000_000   # Practical limit for reasonable performance
    
    def __init__(self, config):
        """
        Initialize the analyzer with category configurations.
        
        Creates category instances based on the configuration dictionary. Supports
        both predefined categories and custom lambda-based rules.
        
        Args:
            config (dict): Configuration dictionary containing category definitions
                Format: {
                    'categories': [
                        {'label': str, 'rule': str},
                        ...
                    ]
                }
                where 'rule' can be:
                - 'even': Numbers divisible by 2
                - 'odd': Numbers not divisible by 2
                - 'prime': Prime numbers
                - lambda expression: Custom rule (e.g., "lambda x: x % 3 == 0")
                
        Example:
            >>> config = {
            ...     'categories': [
            ...         {'label': 'Even', 'rule': 'even'},
            ...         {'label': 'DivBy3', 'rule': 'lambda x: x % 3 == 0'}
            ...     ]
            ... }
            >>> analyzer = NumberAnalyzer(config)
        """
        self.categories = []
        for category_config in config['categories']:
            label = category_config['label']
            rule = category_config['rule']
            
            # Create appropriate category instance based on rule type
            if rule == 'even':
                self.categories.append(Even(label))
            elif rule == 'odd':
                self.categories.append(Odd(label))
            elif rule == 'prime':
                self.categories.append(Prime(label))
            else:
                # For any other rule, treat it as a custom lambda expression
                self.categories.append(CustomCategory(label, rule))
    
    def validate_range(self, min_value, max_value):
        """
        Validate the input range against defined constraints.
        
        Args:
            min_value (int): Start of the range
            max_value (int): End of the range
            
        Returns:
            tuple: (is_valid: bool, message: str)
        """
        # Check system limits
        if min_value < self.MIN_VALUE or max_value > self.MAX_VALUE:
            return False, (
                f"Values must be between {self.MIN_VALUE:,} and {self.MAX_VALUE:,} "
                f"on this system"
            )
            
        if min_value >= max_value:
            return False, "Minimum value must be less than maximum value"
            
        range_size = max_value - min_value + 1
        
        # Warn about ranges beyond practical limits
        if range_size > self.PRACTICAL_LIMIT:
            return False, (
                f"Range size ({range_size:,} numbers) exceeds practical limit of "
                f"{self.PRACTICAL_LIMIT:,}. This might cause performance issues or "
                f"memory errors. Please use a smaller range."
            )
            
        # Warn about large but acceptable ranges
        if range_size > self.RANGE_WARNING:
            return True, (
                f"Warning: Large range detected ({range_size:,} numbers). "
                f"Would you like to save the output to a file? (y/n): "
            )
            
        return True, ""
    
    def analyze_number(self, number):
        """
        Analyze a single number against all categories.
        
        Args:
            number (int): The number to analyze
            
        Returns:
            list[str]: List of category labels that the number matches
            
        Example:
            >>> analyzer.analyze_number(6)
            ['Even', 'DivBy3']
        """
        return [cat.label for cat in self.categories if cat.matches(number)]
    
    def save_to_rtf(self, min_value, max_value, filename=None, output_dir="output"):
        """
        Save the analysis results to an RTF file in the specified output directory.
        
        Args:
            min_value (int): Start of the range
            max_value (int): End of the range
            filename (str, optional): Output filename. If None, generates a default name
            output_dir (str, optional): Name of the output directory. Defaults to "output"
            
        Returns:
            str: Path to the created file
        """
        if filename and os.path.dirname(filename):
            # If filename includes a directory path, use it as is
            full_path = os.path.abspath(filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
        else:
            # Create output directory if it doesn't exist
            results_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), output_dir)
            os.makedirs(results_dir, exist_ok=True)
            
            if filename is None:
                # Generate base filename from range
                base_name = f"range_{min_value}_to_{max_value}"
                
                # Check for existing files with similar names
                counter = 1
                filename = f"{base_name}.rtf"
                full_path = os.path.join(results_dir, filename)
                
                while os.path.exists(full_path):
                    # If file exists, append counter
                    filename = f"{base_name}_{counter}.rtf"
                    full_path = os.path.join(results_dir, filename)
                    counter += 1
            else:
                # If filename is provided without path, save in output directory
                full_path = os.path.join(results_dir, filename)
                
                # If provided filename exists, handle duplicates
                if os.path.exists(full_path):
                    base_name, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(full_path):
                        filename = f"{base_name}_{counter}{ext}"
                        full_path = os.path.join(results_dir, filename)
                        counter += 1
        
        with open(full_path, 'w') as f:
            f.write("{\\rtf1\\ansi\\deff0\n")
            f.write("{\\fonttbl{\\f0\\fnil\\fcharset0 Courier New;}}\n")
            f.write("\\f0\\fs20\n")
            
            # Write header with formatted numbers
            f.write(f"Number Analysis ({min_value:,} to {max_value:,})\\par\n")
            f.write("\\par\n")
            
            # Write results
            for number in range(min_value, max_value + 1):
                labels = self.analyze_number(number)
                f.write(f"{number:,}: {', '.join(labels)}\\par\n")
            
            f.write("}")
            
        return full_path
    
    def run(self, min_value, max_value):
        """
        Analyze all numbers in the specified range.
        
        For each number in the range (inclusive), checks which categories it belongs
        to and prints the results. For large ranges, offers to save output to a file.
        
        Args:
            min_value (int): Start of the range (inclusive)
            max_value (int): End of the range (inclusive)
            
        Example:
            >>> analyzer.run(10, 12)
            10: Even
            11: Prime, Odd
            12: Even, DivBy3
        """
        # Validate the range
        is_valid, message = self.validate_range(min_value, max_value)
        if not is_valid:
            print(f"Error: {message}")
            return
            
        # Handle large ranges
        if message:  # This means we have a warning message
            print(message, end='')
            response = input().lower()
            if response == 'y':
                filepath = self.save_to_rtf(min_value, max_value)
                print(f"Results saved to: {filepath}")
                return
        
        # Print results to console with thousand separators
        for number in range(min_value, max_value + 1):
            labels = self.analyze_number(number)
            print(f"{number:,}: {', '.join(labels)}")
