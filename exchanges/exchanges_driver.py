from bittrex import Bittrex, BOTH_ORDERBOOK


class BitfinexExchangeDriver:
    def __init__(self, config):
        self.client = Client()
        self.account = TradeClient()
        self.balance = None

    def get_balance(self, coin=""):
        return self

    def get_currencies(self):
        return self.client.symbols()

    def get_markets(self):
        return self

    def get_open_orders(self, market):
        return self

    def get_ticker(self, market):
        return self.client.ticker(market)

    def get_orderbook(self, market, book_type=""):
        return self.client.order_book(market)

    def get_market_history(self, market, count):
        return self

    def buy_order(self, market, price, quantity, order_type):
        if order_type == "limit":
            return self
        else:
            return self

    def stop_loss_order(self, market, price, quantity):
        return self

    def sell_order(self, market, price, quantity, order_type):
        if order_type == "limit":
            return self
        else:
            return self

    def cancel_order(self, order):
        return self


class BittrexExchangeDriver:
    def __init__(self, config):
        self.account = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
        self.balance = None

    def get_balance(self, coin=""):
        self.balance = self.account.get_balance(coin)
        return self.balance

    def get_currencies(self):
        return self.account.get_currencies()

    def get_markets(self):
        return self.account.get_markets()

    def get_open_orders(self, market):
        return self.account.get_open_orders(market)

    def get_ticker(self, market):
        return self.account.get_ticker(market)

    # Use constants BUY_ORDERBOOK, SELL_ORDERBOOK, BOTH_ORDERBOOK
    def get_orderbook(self, market, book_type=BOTH_ORDERBOOK):
        return self.account.get_orderbook(market, book_type)

    def get_market_history(self, market, count):
        return self.account.get_market_history(market, count)

    def buy_order(self, market, price, quantity, order_type):
        if order_type == "limit":
            return self.account.buy_limit(market, quantity, price)
        else:
            return self.account.buy_market(market, quantity, price)

    def stop_loss_order(self, market, price, quantity):
        return self

    def sell_order(self, market, price, quantity, order_type):
        if order_type == "limit":
            return self.account.sell_limit(market, quantity, price)
        else:
            return self.account.sell_market(market, quantity, price)

    def cancel_order(self, order):
        return self.account.cancel(order)
