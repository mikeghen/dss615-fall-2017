from etl import CryptoExtractor, FiatExtractor

bitcoin_extractor  = CryptoExtractor("Bitcoin Extractor", "btc", "usd")
litecoin_extractor = CryptoExtractor("Litecoin Extractor", "ltc", "usd")
ltcbtc_extractor   = CryptoExtractor("Litecoin Extractor", "ltc", "btc")

usd_extractor  = FiatExtractor("USD Extractor", "USD")
eur_extractor = FiatExtractor("EUR Extractor", "EUR")
gbp_extractor   = FiatExtractor("GBP Extractor", "GBP")

bitcoin_extractor.execute()
litecoin_extractor.execute()
ltcbtc_extractor.execute()

usd_extractor.execute()
eur_extractor.execute()
gbp_extractor.execute()
