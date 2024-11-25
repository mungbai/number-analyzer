from analyzer.categories.base_category import BaseCategory

class CustomCategory(BaseCategory):
    def __init__(self, label, rule_code):
        super().__init__(label)
        self.rule = eval(rule_code)

    def matches(self, number):
        return self.rule(number)
