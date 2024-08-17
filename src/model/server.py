from flask import Flask, Response, make_response

from cam import Picture
from contour import Contoured
from triangulate import Triangulate
from main import Mask 

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world \n"


@app.route('/get-dimensions')
def image():
    mask = Mask()
    result = mask.get_dimensions()

    return result


if __name__ == "__main__":
    app.run(threaded=True)
