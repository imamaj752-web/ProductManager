from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import re

from models import init_db
from action_db import *

app = Flask(__name__)
app.secret_key = '123'
init_db()

def is_valid_password(password):
    if len(password) < 6:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


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
    if not company:
        session.pop('company_name', None)
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name').lower()
        price = float(request.form.get('price'))
        category = request.form.get('category').lower()

        if product_exist(name, company.id):
            flash('такой товар уже есть!')
        else:
            add_product(name, price, category, company.id)
            flash('товар добавлено')
        return redirect(url_for('index'))

    all_categories = get_all_categories(company.id)
    choice_category = request.args.get('category', 'all')
    filter_products = get_all_products(company.id) if choice_category == 'all' else get_product_by_category(
        choice_category, company.id)

    return render_template('index.html', products=filter_products, categories=all_categories,
                           choice_category=choice_category)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name_company = request.form.get('name_company', '').lower()
        password = request.form.get('password', '')

        if not name_company:
            flash('Логін не може бути порожнім!')
            return redirect(url_for('register'))

        if not is_valid_password(password):
            flash('пароль слышком просто (6+ символов буква цифра, спецсимвол)')
            return redirect(url_for('register'))

        if company_exists(name_company):
            flash('такая компания уже есть')
            return redirect(url_for('register'))

        add_company(name_company, generate_password_hash(password))
        flash(f'компания {name_company} зарегенстирована')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name_company = request.form.get('name_company', '').lower()
        password = request.form.get('password', '')

        if not company_exists(name_company):
            flash(f'компании {name_company} нет')
            return redirect(url_for('login'))

        company = get_company_by_name(name_company)
        if not check_password_hash(company.password, password):
            flash('Пароль некорект')
            return redirect(url_for('login'))

        session['company_name'] = company.name
        flash(f'поздравляем, {company.name}')
        return redirect(url_for('index'))
    return render_template('login.html')


# Кнопка Logout
@app.route('/logout')
def logout():
    session.pop('company_name', None)
    flash("вы вишли из системи")
    return redirect(url_for('login'))


@app.route('/delete/<name>')
def delete(name):
    if not is_logged(): return redirect(url_for('login'))
    company = current_company()
    delete_product(name, company.id)
    flash(f'товар {name} удалено')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)