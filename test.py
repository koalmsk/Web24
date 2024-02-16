import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def main():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)

@app.route('/index')
def index():
    param = {}
    param['username'] = "Вася Пупкин"
    param['title'] = 'Моя страница'
    return render_template('index.html', **param)

@app.route('/odd_even/<num>')
def odd_even(num):
    return render_template('index_jinja.html', number=int(num))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')