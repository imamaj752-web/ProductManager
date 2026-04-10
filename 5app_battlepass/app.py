from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

user_balance = 0
user_inventory = {}

@app.route('/')
def index():
    return render_template('index.html', balance=user_balance)

@app.route('/topup', methods=['GET', 'POST'])
def topup():
    global user_balance
    if request.method == 'POST':
        usd = float(request.form['amount'])
        if usd <= 0:
            flash('Введіть коректну суму')
        elif usd > 1000:
            flash('Максимум для поповнення — 1000 USD')
        else:
            bp = int(usd * 100)
            user_balance += bp
            flash(f'Баланс поповнено на +{bp} BP')
    return render_template('topup.html', balance=user_balance)

app.run(debug=True)
