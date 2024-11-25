# analyzer/categories/custom.py

from analyzer.categories.base_category import BaseCategory

class CustomCategory(BaseCategory):
    def __init__(self, label, rule_code):
        super().__init__(label)
        # Define a safe environment for eval
        allowed_builtins = {'__builtins__': {'all': all, 'int': int, 'range': range}}
        allowed_functions = {'abs': abs, 'math': __import__('math')}
        # Evaluate the lambda expression in a safe environment
        self.rule = eval(f"({rule_code})", {**allowed_builtins, **allowed_functions})

    def matches(self, number):
        try:
            return self.rule(number)
        except Exception as e:
            print(f"Error evaluating custom rule for {self.label}: {e}")
            return False
