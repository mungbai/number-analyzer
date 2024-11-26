"""
Odd Number Category Module

This module provides the implementation for identifying odd numbers.
An odd number is any integer that cannot be divided exactly by 2.

Example:
    1, 3, 5, 7, 9 are odd numbers
    2, 4, 6, 8, 10 are not odd numbers
"""

from .base_category import BaseCategory


class Odd(BaseCategory):
    """
    Category for identifying odd numbers.
    
    Inherits from BaseCategory and implements the matches() method
    to identify numbers that are not divisible by 2 (have a remainder of 1).
    """
    
    def matches(self, number):
        """
        Check if a number is odd.
        
        A number is odd if it is not divisible by 2 (has a remainder of 1).
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is odd, False otherwise
            
        Example:
            >>> odd = Odd("Odd")
            >>> odd.matches(3)
            True
            >>> odd.matches(4)
            False
        """
        return number % 2 == 1
