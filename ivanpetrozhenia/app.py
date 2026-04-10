from flask import Flask, render_template, session, redirect, url_for, request
import random

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.before_request
def setup_session():
    if 'balance' not in session:
        session['balance'] = 0
    if 'inventory' not in session:
        session['inventory'] = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/topup', methods=['GET', 'POST'])
def topup():
    if request.method == 'POST':
        amount = int(request.form.get('amount', 0))
        session['balance'] += amount
        return redirect(url_for('index'))
    return render_template('topup.html')




