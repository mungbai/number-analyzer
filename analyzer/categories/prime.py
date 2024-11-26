"""
Prime Number Category Module

This module provides the implementation for identifying prime numbers.
A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

Example:
    2, 3, 5, 7, 11, 13, 17, 19 are prime numbers
    1, 4, 6, 8, 9, 10, 12, 14, 15, 16 are not prime numbers

Note:
    1 is not considered a prime number by mathematical definition.
    2 is the only even prime number.
"""

from .base_category import BaseCategory
import math

class Prime(BaseCategory):
    """
    Category for identifying prime numbers.
    
    Inherits from BaseCategory and implements the matches() method
    to identify numbers that are prime using an efficient algorithm.
    """
    
    def matches(self, number):
        """
        Check if a number is prime.
        
        A number is prime if it is greater than 1 and has no positive
        divisors other than 1 and itself. This implementation uses an
        efficient algorithm that only checks divisors up to the square
        root of the number.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is prime, False otherwise
            
        Example:
            >>> prime = Prime("Prime")
            >>> prime.matches(17)
            True
            >>> prime.matches(15)
            False
            >>> prime.matches(1)  # 1 is not prime by definition
            False
        """
        # 1 is not prime by definition
        if number < 2:
            return False
            
        # 2 is the only even prime number
        if number == 2:
            return True
            
        # Even numbers greater than 2 cannot be prime
        if number % 2 == 0:
            return False
            
        # Check odd divisors up to the square root
        # We only need to check odd numbers because we already excluded even numbers
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
                
        return True
