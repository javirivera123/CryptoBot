import re


class PatternParser:
    def __init__(self, patterns, data):
        self.data = data
        self.buy_pattern = patterns["regex_buy"].encode("UTF-8")
        self.sell_pattern = patterns["regex_sell"].encode("UTF-8")
        self.stop_pattern = patterns["regex_stop"].encode("UTF-8")
        self.target_pattern = patterns["target"].encode("UTF-8")

    def get_buy_value(self):
        match = re.search(self.buy_pattern, self.data)
        print(self.data)
        if match:
            return match.group()
        else:
            return None

    def get_sell_value(self):
        match = re.search(self.sell_pattern, self.data)
        if match:
            return match.group()
        else:
            return None

    def get_stop_value(self):
        match = re.search(self.stop_pattern, self.data)
        if match:
            return match.group()
        else:
            return None

    def get_target_value(self):
        match = re.search(self.target_pattern, self.data)
        if match:
            return match.group()
        else:
            return None
