"""
Base Category Module

This module provides the foundation for the number analyzer's category system.
It defines the base interfaces and core functionality for categorizing numbers.

Key Components:
- BaseCategory: Abstract base class for all number categories
- NumberAnalyzer: Main orchestrator for number analysis

Author: mungbai
Date: 2024
"""


class BaseCategory:
    """
    Abstract base class that defines the interface for all number categories.
    
    All category implementations (Even, Odd, Prime, Custom) must inherit from this class
    and implement the matches() method.
    
    Attributes:
        label (str): The display name for this category
    """
    
    def __init__(self, label):
        """
        Initialize a new category with a label.
        
        Args:
            label (str): The display name for this category
        """
        self.label = label

    def matches(self, number):
        """
        Check if a number belongs to this category.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number belongs to this category, False otherwise
            
        Raises:
            NotImplementedError: This is an abstract method that must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement matches method")


class NumberAnalyzer:
    """
    Main class that orchestrates the number analysis process.
    
    This class manages all category instances and coordinates the analysis of numbers
    against these categories.
    
    Attributes:
        categories (list[BaseCategory]): List of category instances to check numbers against
    """
    
    def __init__(self, config):
        """
        Initialize the analyzer with category configurations.
        
        Args:
            config (dict): Configuration dictionary containing category definitions
                         Format: {
                             'categories': [
                                 {'label': str, 'rule': str},
                                 ...
                             ]
                         }
                         where 'rule' can be 'even', 'odd', 'prime', or a lambda expression
        """
        self.categories = []
        for category_config in config['categories']:
            label = category_config['label']
            rule = category_config['rule']
            if rule == 'even':
                self.categories.append(Even(label))
            elif rule == 'odd':
                self.categories.append(Odd(label))
            elif rule == 'prime':
                self.categories.append(Prime(label))
            else:
                self.categories.append(CustomCategory(label, rule))

    def run(self, min_value, max_value):
        """
        Analyze numbers in the specified range against all categories.
        
        For each number in the range, this method checks which categories it belongs to
        and prints the results.
        
        Args:
            min_value (int): Start of the range (inclusive)
            max_value (int): End of the range (inclusive)
            
        Example output:
            10: Even, Non-Prime
            11: Prime, Odd
            12: Even, DivBy3, Non-Prime
        """
        for number in range(min_value, max_value + 1):
            labels = [cat.label for cat in self.categories if cat.matches(number)]
            print(f"{number}: {', '.join(labels)}")
