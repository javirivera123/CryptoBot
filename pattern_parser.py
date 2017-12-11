import re


class PatternParser:
    def __init__(self, patterns, data):
        self.data = data
        self.buy_pattern = patterns["regex_buy"]
        self.sell_pattern = patterns["regex_sell"]
        self.stop_pattern = patterns["regex_stop"]
        self.target_pattern = patterns["target"]

    def get_buy_value(self):
        print(self.data)
        match = re.search(self.buy_pattern, self.data)
        if match:
            return match.group(0)
        else:
            return None

    def get_sell_value(self):
        match = re.search(self.sell_pattern, self.data)
        if match:
            return match.group(0)
        else:
            return None

    def get_stop_value(self):
        match = re.search(self.stop_pattern, self.data)
        if match:
            return match.group(0)
        else:
            return None

    def get_target_value(self):
        match = re.search(self.target_pattern, self.data)
        if match:
            return match.group(0)
        else:
            return None
