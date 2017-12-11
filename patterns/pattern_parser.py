import re


class PatternParser:
    def __init__(self, patterns, data):
        self.data = data
        self.buy_pattern = patterns["regex_buy"]
        self.sell_pattern = patterns["regex_sell"]
        self.stop_pattern = patterns["regex_stop"]
        self.target_pattern = patterns["regex_target"]
        self.target_money = patterns["regex_money"]

    def get_buy_value(self):
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

    def get_money_value(self):
        match = re.search(self.target_money, self.data)
        if match:
            return match.group(0)
        else:
            return None

    def parse(self):
        # self.get_target_value()
        sell = self.get_sell_value()
        buy = self.get_buy_value()
        stop = self.get_stop_value()
        money = self.get_money_value()

        if money is not None \
                and sell is not None \
                and buy is not None \
                and stop is not None:
            return [money, buy, stop, sell]
        else:
            raise Exception("Parsing failed")
