from bittrex import Bittrex, API_V2_0

from config.config import load_config


def main():
    config = load_config()

    my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)

    print(my_bittrex.get_balance('BTC'))


main()