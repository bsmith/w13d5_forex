from flask import Flask, render_template, request

from exchange_rate import ExchangeRate

app = Flask(__name__)

@app.route("/")
def home():
    render_template('index.html')

@app.route("/convert", methods=["POST"])
def convert():
    date = request.form['date']
    amount = request.form['amount']
    counterCurrency = request.form['fromCCY']
    baseCurrency = request.form['toCCY']
    convertedAmount = ExchangeRate.at(date, baseCurrency, counterCurrency)
    render_template('result.html',
        date=date,
        amount=amount,
        counterCurrency=counterCurrency,
        baseCurrency=baseCurrency,
        convertedAmount=convertedAmount)

if __name__ == '__main__':
    app.run()