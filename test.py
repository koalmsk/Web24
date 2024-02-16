import json
import os

from PIL import Image
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

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

@app.route('/carousel')
def carousel():
    path = os.path.join('static', 'carousel')
    images=[os.path.join(path, img) for img in os.listdir(path)]
    # чтобы убедиться, что картинки доступны можно их посмотреть
    # for img in images:
    #     opened_image = Image.open(img)
    #     opened_image.show()
    return render_template('carousel_bootstrap.html', img=images)

@app.route('/login')
def login():
    return render_template('login.html', username='Вася')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')