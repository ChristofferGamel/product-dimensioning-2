from flask import Flask, Response, make_response

import sys
sys.path.append('/home/chris/Desktop/product-dimensioning-2/src/')
from models import facades


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world \n"


@app.route('/get-dimensions')
def image():
    mask = facades.DimensionsFacade()
    result = mask.get_dimensions()

    return result

def start_server():
    app.run(threaded=True)


if __name__ == "__main__":
    app.run(threaded=True)
