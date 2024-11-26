"""
Custom Category Module

This module provides the implementation for custom number categories defined by lambda expressions.
It allows users to create their own number categories by specifying rules in the configuration file.

Example:
    A custom category for numbers divisible by 3:
    {
        "label": "DivBy3",
        "rule": "lambda x: x % 3 == 0"
    }
    
    A custom category for perfect squares:
    {
        "label": "Square",
        "rule": "lambda x: int(x**0.5) ** 2 == x"
    }
"""

from analyzer.categories.base_category import BaseCategory


class CustomCategory(BaseCategory):
    """
    Category for custom number rules defined using lambda expressions.
    
    Inherits from BaseCategory and implements the matches() method to evaluate
    custom rules provided as lambda expressions in string format.
    
    Attributes:
        label (str): The display name for this category
        rule_str (str): The lambda expression as a string that defines the rule
        rule_func (callable): The compiled lambda function that implements the rule
    """
    
    def __init__(self, label, rule_str):
        """
        Initialize a custom category with a label and rule.
        
        Args:
            label (str): The display name for this category
            rule_str (str): Lambda expression as a string (e.g., "lambda x: x % 3 == 0")
            
        Raises:
            ValueError: If the rule string is not a valid lambda expression
            SyntaxError: If the rule string contains invalid Python syntax
        """
        super().__init__(label)
        self.rule_str = rule_str
        
        try:
            # Compile the lambda expression into a callable function
            # eval() is safe here because we control the input through the config file
            self.rule_func = eval(rule_str)
        except (ValueError, SyntaxError) as e:
            raise ValueError(f"Invalid rule expression for category '{label}': {rule_str}") from e

    def matches(self, number):
        """
        Check if a number matches the custom rule.
        
        Applies the compiled lambda function to the input number.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number matches the custom rule, False otherwise
            
        Example:
            >>> div_by_3 = CustomCategory("DivBy3", "lambda x: x % 3 == 0")
            >>> div_by_3.matches(9)
            True
            >>> div_by_3.matches(10)
            False
            
            >>> square = CustomCategory("Square", "lambda x: int(x**0.5) ** 2 == x")
            >>> square.matches(16)
            True
            >>> square.matches(15)
            False
        """
        try:
            return bool(self.rule_func(number))
        except Exception as e:
            # If there's an error evaluating the rule, treat it as not matching
            # This prevents errors from breaking the entire analysis
            return False
