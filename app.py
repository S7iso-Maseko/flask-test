from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from CI/CD</h1>"

@app.route('/build')
def build():
    return "<h1>Pipeline Works: CI/CD</h1>"

if __name__ == '__main__':
    app.run(debug=True)