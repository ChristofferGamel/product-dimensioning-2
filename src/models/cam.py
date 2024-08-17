import time
from picamera2 import Picamera2
import cv2
import numpy as np
from gpiozero import LED
from libcamera import controls as Cont

class Picture():
    def __init__(self) -> None:
        self.led = LED(14)

        self.controls = {"AnalogueGain": 1.2, 
                    "Brightness": 0.08,
                    "Sharpness":3,
                    "AwbMode":5,
                    }
        self.picam0 = Picamera2(camera_num=0)
        self.picam1 = Picamera2(camera_num=1)

        config0 = self.picam0.create_preview_configuration(main={"size": (int(2304 * 0.75), int(1296 * 0.75))}, controls=self.controls)
        config1 = self.picam1.create_preview_configuration(main={"size": (int(2304 * 0.75), int(1296 * 0.75))}, controls=self.controls)

        self.picam0.configure(config0)
        self.picam1.configure(config1)

    def picture(self):
        self.led.on()

        self.picam0.start()
        self.picam1.start()

        org_image0 = self.picam0.capture_image()
        org_image1 = self.picam1.capture_image()

        self.led.off()
        self.picam0.close()
        self.picam1.close()

        opencv_image0 = cv2.cvtColor(np.array(org_image0), cv2.COLOR_RGBA2BGR)
        opencv_image1 = cv2.cvtColor(np.array(org_image1), cv2.COLOR_RGBA2BGR)

        opencv_image0 = cv2.flip(opencv_image0, 0)
        opencv_image1 = cv2.flip(opencv_image1, 0)
        
        return opencv_image0, opencv_image1
    
if __name__ == "__main__":
    pic = Picture()
    pic.picture()

