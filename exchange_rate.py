from datetime import date

class ExchangeRate:
    data = None

    @classmethod
    def loadData(self):
        self.data = {}
        self.data['20230126'] = {}
        self.data['20230126']['GBP'] = 0.8794
        self.data['20230126']['USD'] = 1.0895

    @classmethod
    def at(self, date, baseCurrency, counterCurrency):
        if self.data is None:
            self.loadData()
        dateStr = date.strftime("%Y%m%d")
        return self.data[dateStr][baseCurrency] / self.data[dateStr][counterCurrency]