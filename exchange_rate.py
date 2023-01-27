from datetime import date
from xml.dom.minidom import parse

xmlnsEurofxref = "http://www.ecb.int/vocabulary/2002-08-01/eurofxref"
xmlnsGesmes = "http://www.gesmes.org/xml/2002-08-01"

def _processXml(dom):
    # structure is: /gesmes:Envelope/Cube/Cube[@time]/Cube[@currency,@rate]
    envelope = dom.getElementsByTagNameNS(xmlnsGesmes, "Envelope")[0]
    return _handleEnvelope(envelope)

def _handleEnvelope(envelope):
    # handle the first <Cube> inside the Envelope
    for node in envelope.childNodes:
        if node.namespaceURI == xmlnsEurofxref and node.tagName == "Cube":
            return _handleTopCube(node)

def _handleTopCube(cube):
    dataByDate = {}
    # the next nodes down are Cubes per date
    for node in cube.childNodes:
        if node.namespaceURI == xmlnsEurofxref and node.tagName == "Cube":
            time = node.getAttribute('time')
            dataByDate[time] = _handleTimeCube(node)
    return dataByDate

def _handleTimeCube(cube):
    dataByCurrency = {}
    for node in cube.childNodes:
        if node.namespaceURI == xmlnsEurofxref and node.tagName == "Cube":
            currency = node.getAttribute('currency')
            rate = float(node.getAttribute('rate'))
            dataByCurrency[currency] = rate
    return dataByCurrency

class ExchangeRate:
    data = None

    @classmethod
    def loadData(self):
        # self.data = {}
        # self.data['2023-01-26'] = {}
        # self.data['2023-01-26']['GBP'] = 0.8794
        # self.data['2023-01-26']['USD'] = 1.0895
        dom = parse('example-20230127.xml')
        self.data = _processXml(dom)

    @classmethod
    def at(self, date, baseCurrency, counterCurrency):
        if self.data is None:
            self.loadData()
        dateStr = date.strftime("%Y-%m-%d")
        return self.data[dateStr][baseCurrency] / self.data[dateStr][counterCurrency]