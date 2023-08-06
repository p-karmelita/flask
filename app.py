from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    name = request.form['name']
    age = request.form['age']
    score = request.form['score']
    return render_template('send.html', name=name, age=age, score=score)


if __name__ == '__main__':
    app.run(debug=True)
