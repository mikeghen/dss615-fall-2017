from recursive import flatten_dict
import urllib2
import json

DATA_DIRECTORY = '/var/data'

class Extractor(object):
    """
    Generalized object for pulling data from a URL endpoint.
    """

    DATA_DIRECTORY = '/var/data'

    def __init__(self, name):
        self.name     = name
        self.data     = None
        self.records  = None
        self.path   = None

    def execute(self):
        """
        Executes the extract, transform, and load flow
        """
        self.data    = self.extract()
        self.records = self.transform()
        self.path  = self._load()
        print("Extracted, transformed, and loaded for %s" % self.name)

    def extract(self):
        """
        Extracts data from a url.
        """
        extracted_data = []

        response        = urllib2.urlopen(self.url)
        extracted_data  = json.load(response)

        return extracted_data

    def transform(self):
        """
        Subclasses will implement this function using custom logic.
        Must return a list of tuples.
        """
        raise NotImplementedError('Subclasses must override the _transform method.')

    def __load(self):
        """
        Writes tuple records to file at DATA_FILE_PATH as TSV. Returns the number of
        records written to the file.
        """
        # Validate that we have a list of tuples.
        if not isinstance(self.records, list):
            for record in self.records:
                if not isinstance(record, tuple):
                    raise TypeError('Can not load anything other than a list of tuples.')

        record_counter = 0
        path = "%s/%s.data" % (DATA_DIRECTORY, self.name)


        with open(path, 'a+') as data_file:
            for record in self.records:
                # Write 1 record per line
                data_file.write('\t'.join(map(str,record)))
                data_file.write('\n')
                record_counter += 1

        return path

class CryptoExtractor(Extractor):
    def __init__(self, name, base, target):
        super(CryptoExtractor, self).__init__(name)
        self.url = "https://api.cryptonator.com/api/full/%s-%s"%(base,target)

    def transform(self):
        """
        Transforms data dictionary into tuples to insert into a database:
            - btc_markets.table: (timestamp, market, price_usd, volume)
        Returns an array of tuples, one tuple for each record
        """
        ticker_data         = self.data["ticker"]
        timestamp           = self.data["timestamp"]
        base                = ticker_data["base"]
        target              = ticker_data["target"]
        markets_records = []

        for market_record in ticker_data["markets"]:
            record_tuple = (timestamp, base, target, market_record["market"], market_record["price"], market_record["volume"])
            markets_records.append(record_tuple)

        return markets_records

class FiatExtractor(Extractor):
    def __init__(self, name, base):
        super(FiatExtractor, self).__init__(name)
        self.url = "http://api.fixer.io/latest?base=%s"%(base)

    def transform(self):
        """
        Transforms data dictionary into tuples to insert into a database.

        date, base, target, rate

        """

        date         = self.data["date"]
        base         = self.data["base"]

        markets_records = []
        for key, value in self.data["rates"].items():
            record_tuple = (date, base, key, value)
            markets_records.append(record_tuple)

        return markets_records
