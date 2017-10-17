from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)


@app.route('/')
def index():

    response        = urllib2.urlopen('https://api.cryptonator.com/api/full/btc-usd')
    data  = json.load(response)

    ticker_data         = data["ticker"]
    timestamp           = data["timestamp"]
    btc_markets_records = []

    for market_record in ticker_data["markets"]:
        record_tuple = (timestamp, market_record["market"], market_record["price"], market_record["volume"])
        btc_markets_records.append(record_tuple)

    return render_template('index.html', records=btc_markets_records)


if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)
