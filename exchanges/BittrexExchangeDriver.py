from bittrex import Bittrex


class BittrexExchangeDriver:
    def __init__(self, config):
        self.account = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
        self.balances = None

    def get_balance(self, coin=""):
        if coin == "":
            return self.account.get_balance(coin)
        else:
            self.balances = self.account.get_balances()
            return self.balances

    def get_currencies(self):
        return self.account.get_currencies()

    def get_open_orders(self, market):
        return self.account.get_open_orders(market)

    def get_ticker(self, market):
        return self.account.get_ticker(market)

    # Use constants BUY_ORDERBOOK, SELL_ORDERBOOK, BOTH_ORDERBOOK
    def get_orderbook(self, symbol, book_type=BOTH_ORDERBOOK):
        return self.account.get_orderbook(symbol, book_type)

    def get_market_history(self, symbol, count):
        return self.account.get_market_history(symbol, count)

    # symbol = BTC-LTC
    def buy_order(self, symbol, price, quantity, order_type):
        if order_type == "limit":
            return self.account.buy_limit(symbol, quantity, price)
        else:
            return self.account.buy_market(symbol, quantity, price)

    def stop_loss_order(self, market, price, quantity):
        return None

    def sell_order(self, symbol, price, quantity, order_type):
        if order_type == "limit":
            return self.account.sell_limit(symbol, quantity, price)
        else:
            return self.account.sell_market(symbol, quantity, price)

    def cancel_order(self, order):
        return self.account.cancel(order)