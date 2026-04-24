from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from models import init_db
from action_db import *
from action_db import delete_product_by_name

app = Flask(__name__)
app.secret_key = '123'
init_db()


def is_logged():
    return 'company_name' in session


@app.route('/', methods=['GET', 'POST'])
def index():
    if not is_logged():
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name').lower()
        price = float(request.form.get('price'))
        category = request.form.get('category').lower()

        if product_exist(name):
            flash('Такий товар вже є!')
        else:
            add_product(name, price, category)
            flash('Товар додано!')

        return redirect(url_for('index'))

    all_categories = get_all_categories()

    choice_category = request.args.get('category', 'all')

    if choice_category == 'all':
        filter_products = get_all_products()
    else:
        filter_products = get_product_by_category(choice_category)

    return render_template('index.html',
                           products=filter_products,
                           categories=all_categories,
                           choice_category=choice_category)

@app.route('/delete_product', methods=['POST'])
def delete_product():
    name = request.form.get('name')
    if name:
        delete_product_by_name(name)
        flash(f'Товар {name} видалено!') # Можна додати повідомлення
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name_company = request.form.get('name_company').lower()
        password = request.form.get('password')

        if company_exists(name_company):
            flash('Така компанія вже є!')
            return redirect(url_for('register'))
        else:
            password_hash = generate_password_hash(password)

            flash(f'Компанія {name_company} зареєстрована!')
            add_company(name_company, password_hash)

            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name_company = request.form.get('name_company').lower()
        password = request.form.get('password')

        if not company_exists(name_company):
            flash(f'Компанія {name_company} НЕ ІСНУЄ!')
            return redirect(url_for('login'))

        company = get_company_by_name(name_company)
        if not check_password_hash(company.password, password):
            flash(f'Пароль НЕкоректний')
            return redirect(url_for('login'))

        session['company_name'] = company.name

        flash(f'Вітаємо, {company.name}!')
        return redirect(url_for('index'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
