import unittest
from datetime import datetime

def stockSymbol(symbol):
    if not symbol.isalpha():
        return False
    if len(symbol) < 1 or len(symbol) > 7:
        return False
    if not symbol.isupper():
        return False
    return True

def chartType(chartType):
    return chartType in ('1', '2')

def timeSeries(timeSeries):
    return timeSeries in ('1', '2', '3', '4')

def chartDates(dates):
    try:
        datetime.strptime(dates, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class TestInputs(unittest.TestCase):

    def test_stockSymbol(self):
        self.assertTrue(stockSymbol("AAPL"))

    def test_chartType(self):
        self.assertTrue(chartType("1"))

    def test_timeSeries(self):
        self.assertTrue(timeSeries("1"))

    def test_chartDate1(self):
        self.assertTrue(chartDates("2024-04-22"))

    def test_chartDate2(self):
        self.assertTrue(chartDates("2024-04-22"))

if __name__ == "__main__":
    unittest.main()