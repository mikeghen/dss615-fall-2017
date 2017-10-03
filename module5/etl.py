"""
USAGE:

from etl import extract, transform, load
btc_data = extract()
markets_records = transform(btc_data)
written_records = load(markets_records)

"""

import urllib2
import json

DATA_FILE_PATH = 'data/btc_markets.table'

def extract():
    """
    Extracts data from a URL. Returns the data extracted as a dictionary.
    """
    URL = 'https://api.cryptonator.com/api/full/btc-usd'

    extracted_data = []

    # Get JSON data from the URL
    response        = urllib2.urlopen(URL)
    extracted_data  = json.load(response)

    return extracted_data

def transform(data):
    """
    Transforms data dictionary into tuples to insert into a database:
        - btc_markets.table: (timestamp, market, price_usd, volume)
    Returns an array of tuples, one tuple for each record
    """

    ticker_data         = data["ticker"]
    timestamp           = data["timestamp"]
    btc_markets_records = []

    for market_record in ticker_data["markets"]:
        record_tuple = (timestamp, market_record["market"], market_record["price"], market_record["volume"])
        btc_markets_records.append(record_tuple)

    return btc_markets_records

def load(records):
    """
    Writes tuple records to file at DATA_FILE_PATH as TSV. Returns the number of
    records written to the file.
    """
    record_counter = 0

    with open(DATA_FILE_PATH, 'a+') as data_file:
        for record in records:
            # Write 1 record per line
            data_file.write('\t'.join(map(str,record)))
            data_file.write('\n')
            record_counter += 1

    return record_counter
