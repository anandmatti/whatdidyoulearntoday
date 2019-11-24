from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "{message:'What did you learn today application'}"


@app.route("/learn")
def learn():
    return "{question:'What did you learn today?'}"


if __name__ == '__main__':
    app.run()

