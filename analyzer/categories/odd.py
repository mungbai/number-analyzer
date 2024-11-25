# analyzer/categories/odd.py

from analyzer.categories.base_category import BaseCategory

class Odd(BaseCategory):
    def matches(self, number):
        return number % 2 != 0
