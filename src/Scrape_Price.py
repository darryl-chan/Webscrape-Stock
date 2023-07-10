import yfinance as yf

def scrape_price(stock, year=5):
    """Gets stock price data 

    Args:
        stock (str): Stock name in shortened
        year (int, optional): Time period. Defaults to 5 years.

    Returns:
        _type_: _description_
    """
    period = '{}y'.format(year)
    # Request historical data for past 5 years
    data = yf.Ticker(stock).history(period=period)
    # Show info
    return data


def get_close(stock, year=5):
    data = scrape_price(stock, year)
    new_data = data['Close']
    return new_data