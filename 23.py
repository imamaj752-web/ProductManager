from flask import Flask, request, render_template_string

app = Flask(__name__)

# Шаблон HTML-страницы
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Твій букет тюльпанів</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f9f9f9; }
        .result { margin-top: 30px; white-space: pre; font-family: monospace; }
        input[type="number"] { width: 60px; padding: 5px; }
        button { padding: 5px 15px; margin-left: 10px; }
    </style>
</head>
<body>
    <h1>Твій букет тюльпанів</h1>
    <p>Ціна за 1 тюльпан - 60 грн</p>

    <form method="POST">
        <label for="count">Кількість тюльпанів:</label>
        <input type="number" name="count" id="count" min="1" max="20" required>
        <button type="submit">Відправити</button>
    </form>

    {% if result %}
    <div class="result">
        {{ result }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/tulips', methods=['GET', 'POST'])
def tulips():
    result = None
    if request.method == 'POST':
        try:
            count = int(request.form.get('count', 0))
            if count < 1 or count > 20:
                result = "Будь ласка, введіть число від 1 до 20."
            else:
                total_price = count * 60
                # Генеруємо піраміду з тюльпанів
                pyramid = ""
                for i in range(1, count + 1):
                    pyramid += "🌷" * i + "\n"
                result = f"Ваш букет коштує: {total_price} грн\n\n{pyramid}"
        except ValueError:
            result = "Будь ласка, введіть коректне число."

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)