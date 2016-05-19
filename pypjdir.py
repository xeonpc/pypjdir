from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h>Hello World!</h>'
            '<p>哈哈哈</p>')


if __name__ == '__main__':
    app.run()
