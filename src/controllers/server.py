from flask import Flask, Response, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world \n'


if __name__ == '__main__':
    app.run(threaded=True)