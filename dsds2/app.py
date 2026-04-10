from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/tulips', methods=['GET', 'POST'])
def tulips():
    cost = pyramid = ""
    if request.method == 'POST':
        n = int(request.form['count'])
        cost = n * 60
        pyramid = "<br>".join("🌷" * i for i in range(1, n + 1))
    return render_template('tulips.html', cost=cost, pyramid=pyramid)

if __name__ == '__main__':
    app.run(debug=True)