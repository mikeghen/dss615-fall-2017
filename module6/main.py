from etl import extract, transform, load

# TRY:
# http://api.fixer.io/latest
# https://api.cryptonator.com/api/full/ltc-usd
# https://google.com

url   = raw_input("Enter a URL that returns JSON: ")

raw_data, error = extract(url)

if error is None:
    records = transform(raw_data)
    count = load(records)
    print("Loaded %d records from %s" % (count, url))
else:
    print("An error occured: %s" % error['message'])
