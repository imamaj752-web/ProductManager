from flask import Flask, render_template
import random

# створення об'єкту додатку
app = Flask(__name__)


# маршрут головної сторінки
@app.route('/')
@app.route('/home')
def index():
    # render_template() - відображає HTML-шаблон
    return render_template('index.html', name='Lera')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/teachers')
def teachers():
    names = ['Petro', 'Vlad', 'Zhenia']
    return render_template('teachers.html', teachers=names)


@app.route('/surprise')
def surprise():
    is_win = random.choice([True, False])
    discount = random.randint(500, 10000)
    return render_template('surprise.html', is_win=is_win, discount=discount)


# запуск додатку
app.run(debug=True)