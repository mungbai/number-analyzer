"""
Even Number Category Module

This module provides the implementation for identifying even numbers.
An even number is any integer that can be divided exactly by 2.

Example:
    2, 4, 6, 8, 10 are even numbers
    1, 3, 5, 7, 9 are not even numbers
"""

from .base_category import BaseCategory


class Even(BaseCategory):
    """
    Category for identifying even numbers.
    
    Inherits from BaseCategory and implements the matches() method
    to identify numbers that are divisible by 2 with no remainder.
    """
    
    def matches(self, number):
        """
        Check if a number is even.
        
        A number is even if it is divisible by 2 with no remainder.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is even, False otherwise
            
        Example:
            >>> even = Even("Even")
            >>> even.matches(4)
            True
            >>> even.matches(7)
            False
        """
        return number % 2 == 0
