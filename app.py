from flask import Flask, render_template, request
from datetime import datetime

from exchange_rate import ExchangeRate

app = Flask(__name__)

ExchangeRate.loadData()
currencies = list(ExchangeRate.data["2023-01-26"].keys())

@app.route("/")
def home():
    return render_template('index.html', currencies=currencies)

@app.route("/convert", methods=["POST"])
def convert():
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")
    amount = request.form['amount']
    counterCurrency = request.form['fromCCY']
    baseCurrency = request.form['toCCY']
    convertedAmount = ExchangeRate.at(date, baseCurrency, counterCurrency)
    return render_template('result.html',
        date=date,
        amount=amount,
        counterCurrency=counterCurrency,
        baseCurrency=baseCurrency,
        convertedAmount=convertedAmount)

if __name__ == '__main__':
    app.run()