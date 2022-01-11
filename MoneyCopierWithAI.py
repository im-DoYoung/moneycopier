import time
from typing import ByteString
import pyupbit
from pandas import DataFrame
import datetime

access = "a5zak8Vs0M69jtRWYvXZFysfgLRtxhgkgGnOdHMH"
secret = "RSzxbn37cbLxWxYU3yBYmZcciMuoJcVSzO6EtBCs"
upbit = pyupbit.Upbit(access, secret)
print("Loged In")

krw = upbit.get_balance("KRW")
print(krw)

krw_tickers = pyupbit.get_tickers("KRW")

while True:
    while predict_price(best_ticker)>pyupbit.get_current_price(best_ticker)*1.05:
        try:
            for best_ticker in krw_tickers:
                def predict_price(best_ticker):
                    global predicted_close_price
                    df = pyupbit.get_ohlcv(best_ticker, interval="minute60")
                    df = df.reset_index()
                    df['ds'] = df['index']
                    df['y'] = df['close']
                    data = df[['ds','y']]
                    model = Prophet()
                    model.fit(data)
                    future = model.make_future_dataframe(periods=24, freq='H')
                    forecast = model.predict(future)
                    closeDf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]
                    if len(closeDf) == 0:
                        closeDf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]
                    closeValue = closeDf['yhat'].values[0]
                    predicted_close_price = closeValue
                    predict_price(best_ticker)
                    schedule.every().hour.do(lambda: predict_price(best_ticker))
        except AttributeError: print(AttributeError)

    if krw>5000:
        upbit.buy_market_order(best_ticker, krw*0.995)
        print("bought", best_ticker)                
    else:
        if predict_price(best_ticker)<pyupbit.get_current_price(best_ticker):
            price_crypto = upbit.get_balance(best_ticker)
            if price_crypto > 0:
                upbit.sell_market_order(best_ticker, price_crypto) 
                print("sold", best_ticker) 







