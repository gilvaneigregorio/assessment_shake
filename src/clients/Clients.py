from clients.external.CurrencyProvider import CurrencyDataAPI

def getCurrencyProvider(is_test: bool| None = None):
    return CurrencyDataAPI