from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from models import init_db
from action_db import *

app = Flask(__name__)
app.secret_key = '123'
init_db()


def is_valid_password(password):
    if len(password) < 6:
        return False

    has_letter = False
    has_digit = False
    has_spec = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_spec = True

    return has_letter and has_digit and has_spec


def is_logged():
    return 'company_name' in session


def current_company():
    name_company = session.get('company_name')
    if not name_company:
        return None
    return get_company_by_name(name_company)


@app.route('/', methods=['GET', 'POST'])
def index():
    if not is_logged():
        return redirect(url_for('login'))

    company = current_company()

    if request.method == 'POST':
        name = request.form.get('name').lower()
        price = float(request.form.get('price'))
        category = request.form.get('category').lower()

        if product_exist(name, company.id):
            flash('Такий товар вже є!')
        else:
            add_product(name, price, category, company.id)
            flash('Товар додано!')

        return redirect(url_for('index'))

    all_categories = get_all_categories(company.id)
    choice_category = request.args.get('category', 'all')

    if choice_category == 'all':
        filter_products = get_all_products(company.id)
    else:
        filter_products = get_product_by_category(choice_category, company.id)

    return render_template('index.html',
                           products=filter_products,
                           categories=all_categories,
                           choice_category=choice_category)


@app.route('/delete/<name>')
def delete(name):
    if not is_logged():
        return redirect(url_for('login'))

    company = current_company()
    delete_product(name, company.id)

    flash(f'Товар {name} - видалено!')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name_company = request.form.get('name_company').lower()
        password = request.form.get('password')

        if not name_company:
            flash('Логін не може бути порожнім!')
            return redirect(url_for('register'))

        if not is_valid_password(password):
            flash('Пароль має містити: 6+ символів, літеру, цифру та спецсимвол.')
            return redirect(url_for('register'))

        if company_exists(name_company):
            flash('Така компанія вже є!')
            return redirect(url_for('register'))
        else:
            password_hash = generate_password_hash(password)
            add_company(name_company, password_hash)
            flash(f'Компанія {name_company} зареєстрована!')
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


@app.route('/logout')
def logout():
    session.pop('company_name', None)
    flash("Ви вийшли з системи")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)