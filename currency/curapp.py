from flask import Flask, render_template, request
import requests

curapp = Flask(__name__)

@curapp.route('/')
def home():
    return render_template('index.html')

@curapp.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    base_currency = request.form['base_currency']
    target_currency = request.form['target_currency']

    # Make API request to obtain exchange rate
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
    data = response.json()
    exchange_rate = data['rates'][target_currency]

    # Calculate converted amount
    converted_amount = round(amount * exchange_rate, 2)

    return render_template('result.html', amount=amount, base_currency=base_currency, target_currency=target_currency, converted_amount=converted_amount)

if __name__ == '__main__':
    curapp.run()
