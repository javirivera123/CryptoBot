from bittrex import Bittrex, BOTH_ORDERBOOK

from exchanges.bitfinex_client import TradeClient, Client


class BitfinexExchangeDriver:
    def __init__(self, config):
        self.client = Client()
        self.account = TradeClient(config["bitfinex-key"]["key"], config["bitfinex-key"]["secret"])
        self.balances = None

    def get_balance(self, coin=""):
        self.balances = self.account.balances()
        return self.balances

    def get_currencies(self):
        return self.client.symbols()

    def get_open_orders(self, market):
        return self.account.active_orders()

    def get_ticker(self, market):
        return self.client.ticker(market)

    def get_orderbook(self, market, book_type=""):
        return self.client.order_book(market)

    def get_market_history(self, market, count=0):
        return self.account.history(market, since=count)

    def buy_order(self, market, price, quantity, order_type):
        return self.account.place_order(amount=quantity, price=price, symbol=market, side="buy",
                                        ord_type="exchange " + order_type)

    def stop_loss_order(self, market, price, quantity):
        return self.account.place_order(amount=quantity, price=price, symbol=market, side="sell",
                                        ord_type="exchange stop")

    def sell_order(self, market, price, quantity, order_type):
        return self.account.place_order(amount=quantity, price=price, symbol=market, side="sell",
                                        ord_type="exchange " + order_type)

    def cancel_order(self, order):
        return self.account.delete_order(order)


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
        return None

    def sell_order(self, market, price, quantity, order_type):
        if order_type == "limit":
            return self.account.sell_limit(market, quantity, price)
        else:
            return self.account.sell_market(market, quantity, price)

    def cancel_order(self, order):
        return self.account.cancel(order)
