from recursive import flattenDict
import urllib2
import json

DATA_FILE_PATH = 'data/markets.table'

def extract(url):
    """
    Extracts data from a url. Returns the data extracted as a dictionary.
    If there is an error, it returns the error as a dictionary.
    """
    extracted_data = []
    error = None

    try:
        response        = urllib2.urlopen(url)
        extracted_data  = json.load(response)
    except ValueError as e:
        error = {'message': str(e)}
    except urllib2.HTTPOpenError as e:
        error = {'message': "There's no internet"}


    return extracted_data, error

def transform(data):
    """
    Transforms data dictionary into tuples to insert into a database:
        - btc_markets.table: (timestamp, market, price_usd, volume)
    Returns an array of tuples, one tuple for each record
    """
    print(flattenDict(data))
    ticker_data         = data["ticker"]
    timestamp           = data["timestamp"]
    base                = ticker_data["base"]
    target              = ticker_data["target"]
    btc_markets_records = []

    for market_record in ticker_data["markets"]:
        record_tuple = (timestamp, base, target, market_record["market"], market_record["price"], market_record["volume"])
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
