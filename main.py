from bittrex import Bittrex

def main():
    config = load_config()

    my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version="API_V2_0")

    my_bittrex.get_balance('BTC')