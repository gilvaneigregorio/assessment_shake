from clients.external.currency_provider import CurrencyDataAPI


def getCurrencyProvider(is_test: bool | None = None):
    return CurrencyDataAPI
