import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/hello')
def hello():
    return 'I am good, how about you?'

@app.route('/sentry-test')
def sentry_test():
    1 / 0
    return 'sentry is awesome!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
