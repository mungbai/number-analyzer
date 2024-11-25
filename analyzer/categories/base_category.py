from analyzer.categories import Even, Odd, Prime, CustomCategory

class NumberAnalyzer:
    def __init__(self, config):
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
        for number in range(min_value, max_value + 1):
            labels = [cat.label for cat in self.categories if cat.matches(number)]
            print(f"{number}: {', '.join(labels)}")
