import cv2
import numpy as np
from picamera2 import Picamera2
from rembg import remove
import time

from models.cam import Picture
from models.contour import Contoured
from models.triangulate import Triangulate

class PicturesFacade():
    def __init__(self) -> None:
        self.cam = Picture()

    def take_pictures(self):
        cam_0, cam_1 = self.cam.picture()
        pictures = {"cam_0":cam_0, "cam_1":cam_1}
        return pictures

class ContourFacade():
    def __init__(self) -> None:
        pass

    def apply_contour(self, pictures, testing):
        image_0 = pictures['cam_0']
        image_1 = pictures['cam_1']

        left = image_0
        right = image_1

        left_image =  Contoured(left, testing, "left")
        right_image = Contoured(right, testing, "right")

        left_image.contoured()
        right_image.contoured()

        left = left_image.properties()
        right = right_image.properties()

        return left, right

class TriangulateFacade():
    def __init__(self) -> None:
        self.triangulate = Triangulate()
        self.dist = 39.0

    def triangulate_dimensions(self, left_properties, right_properties):
        dist = self.dist
        width, depth, height = self.triangulate.object_size(dist, left_properties, right_properties)
        return width, depth, height

class DimensionsFacade():
    def __init__(self) -> None:
        self.time = time.time()
        self.pictures_facade = PicturesFacade()
        self.contour_facade = ContourFacade()
        self.triangulate_facade = TriangulateFacade()

    def get_dimensions(self, testing=False):
        pictures = self.pictures_facade.take_pictures()
        left_properties, right_properties = self.contour_facade.apply_contour(pictures, testing)
        w, d, h = self.triangulate_facade.triangulate_dimensions(left_properties, right_properties)

        dimensions_dictionairy = {"width":w,"depth":d,"height":h}

        print ("Time: ", time.time()-self.time)

        return dimensions_dictionairy

if __name__ == "__main__":
    dim = DimensionsFacade()
    result = dim.get_dimensions()

    print(result)