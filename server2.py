from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

popular_tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA", "NVDA", "AMD", "BA", "PYPL", "MS"]

def get_stock_info(tickers):
    # Pusta ramka danych do przechowywania informacji
    stocks_df = [["Symbol", "Company Name", "Current Price", "Change $", "Change %", "Volume"]]

    for ticker in tickers:
        stock_info = yf.Ticker(ticker)
        info_dict = stock_info.info
        #print(info_dict)
        current_price = info_dict["currentPrice"]
        previous_close = info_dict["previousClose"]
        volume = info_dict["volume"]

        change_dollar = current_price - previous_close
        change_percent = (change_dollar / previous_close) * 100

        stocks_df.append([
            ticker,
            info_dict['shortName'],
            current_price,
            change_dollar,
            change_percent,
            volume])

    return stocks_df


@app.route('/', methods=['POST', 'GET'])
def index():

    tbl = get_stock_info(popular_tickers)

    return render_template("main2.html", table= tbl)


