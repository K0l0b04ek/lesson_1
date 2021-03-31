from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/Готовися к миссии')
def index():
    param = {}
    param['text1'] = 'Миссия Колонизация Марса'
    param['text4'] = 'И на Марсе будут яблони цвести!'
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training(prof):
    prof = prof.lower()
    return render_template('index.html', title=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
