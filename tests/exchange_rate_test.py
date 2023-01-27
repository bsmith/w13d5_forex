import unittest
from datetime import date

from exchange_rate import ExchangeRate

class TestExchangeRate(unittest.TestCase):
    def setUp(self):
        pass

    def test_at_example_1(self):
        # GBP is the base currency and USD is the counter currency
        # returns how many GBP one USD is worth
        rate = ExchangeRate.at(date(2023,1,26), 'GBP', 'USD')
        # from example.xml:
        #   20230126 1 EUR = 0.8794 GBP
        #   20230126 1 EUR = 1.0895 USD
        # (1 USD) / (1.0895 USD/EUR) * (0.8794 GBP/EUR)
        self.assertAlmostEqual(0.80716, rate, places=4)