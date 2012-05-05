import os

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    files = os.listdir('static/img/home')
    images = ['/static/img/home/' + file for file in files if file.endswith('.png')]
    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)