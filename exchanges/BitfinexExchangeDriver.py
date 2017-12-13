from exchanges.BitfinexClient import TradeClient, Client


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

    # symbol = BTCUSD
    def buy_order(self, symbol, price, quantity, order_type):
        return self.account.place_order(amount=quantity, price=price, symbol=symbol, side="buy",
                                        ord_type="exchange " + order_type)

    def stop_loss_order(self, symbol, price, quantity):
        return self.account.place_order(amount=quantity, price=price, symbol=symbol, side="sell",
                                        ord_type="exchange stop")

    def sell_order(self, symbol, price, quantity, order_type):
        return self.account.place_order(amount=quantity, price=price, symbol=symbol, side="sell",
                                        ord_type="exchange " + order_type)

    def cancel_order(self, order):
        return self.account.delete_order(order)