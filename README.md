# CryptoBot

## Install
### Prerequisites
- Register to [Telegram](https://telegram.org)
- Get Telegram API (id and hash) : [Telegram API](https://core.telegram.org/api/obtaining_api_id)

### Installation
Get the project sources
```
git clone https://github.com/Herklos/CryptoBot
cd CryptoBot-Telegram
pip install -r requirements.txt
```
Configuration<br>
- *Copy config/default_config.json --> config/config.json*
- Change **telegram-api**
```
"telegram-api":{
    "api_id" : "YOUR_API_ID",
    "api_hash" : "YOUR_API_HASH",
    "phone_number" : "+33122334455"
  }
```
- (Optional) Change **bittrex-key**
```
"bittrex-key": {
    "key" : "YOUR_BITTREX_API_KEY",
    "secret" : "YOUR_BITTREX_API_SECRET"
  },
```

## Usage
### Backtesting (Working)
```
python main.py --backtest
```
### RealTime trading (Working)
```
python main.py --realtrade
```

## Development
TODO
