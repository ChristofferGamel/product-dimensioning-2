from flask import Flask, Response, make_response
from src.model.contour import Contoured as Contour
from cam import Picture



app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world \n"


@app.route("/image")
def image():
    cam_0 = Picture.picture(0)
    cam_1 = Picture.picture(1)

    contour_0 = Contour(cam_0)
    contour_1 = Contour(cam_1)

    print(contour_0.properties())
    print(contour_1.properties())

    return "something \n"


if __name__ == "__main__":
    app.run(threaded=True)
