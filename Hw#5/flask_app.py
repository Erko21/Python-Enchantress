from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello my name is Ernest and it is my flask app'


@app.route('/info')
def info():
    return 'Trying docker'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
