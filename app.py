import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/")
def hello():
    return "{message:'What did you learn today application'}"


@app.route("/learn")
def learn():
    return "{question:'What did you learn today?'}"


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()

