from analyzer.categories.base_category import BaseCategory

class Even(BaseCategory):
    def matches(self, number):
        return number % 2 == 0
