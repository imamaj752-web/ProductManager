from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# Наш порожній словник для товарів
products = {}


@app.route('/products', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        price = request.form.get('price')
        category = request.form.get('category')

        # Логіка перевірки: чи є вже такий товар
        if name in products:
            flash('Такий товар вже є!')
        else:
            # Додаємо в словник
            products[name] = {'price': price, 'category': category}

        return redirect(url_for('index'))

    # Передаємо словник products у шаблон HTML
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)