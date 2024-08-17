import time
from picamera2 import Picamera2
import cv2
import numpy as np
from gpiozero import LED
from libcamera import controls as Cont

class Picture():
    def __init__(self) -> None:
        self.controls = {"AnalogueGain": 1.2, 
                    "Brightness": 0.08,
                    "Sharpness":3,
                    "AwbMode":5,
                    }

    def picture(self):
        led = LED(14)
        picam0 = Picamera2(camera_num=0)
        picam1 = Picamera2(camera_num=1)
        controls = {"AnalogueGain": 1.2, 
                    "Brightness": 0.08,
                    "Sharpness":3,
                    "AwbMode":5,
                    }
        config = picam0.create_preview_configuration(main={"size": (int(2304 * 0.75), int(1296 * 0.75))}, controls=self.controls)
        config = picam1.create_preview_configuration(main={"size": (int(2304 * 0.75), int(1296 * 0.75))}, controls=self.controls)
        picam0.configure(config)
        picam1.configure(config)

        # led.on()

        picam0.start()
        picam1.start()

        org_image0 = picam0.capture_image()
        org_image1 = picam1.capture_image()

        # led.off()
        picam0.close()
        picam1.close()

        opencv_image0 = cv2.cvtColor(np.array(org_image0), cv2.COLOR_RGBA2BGR)
        opencv_image1 = cv2.cvtColor(np.array(org_image1), cv2.COLOR_RGBA2BGR)

        opencv_image0 = cv2.flip(opencv_image0, 0)
        opencv_image1 = cv2.flip(opencv_image1, 0)
        
        return opencv_image0, opencv_image1
    
if __name__ == "__main__":
    pic = Picture()
    pic.picture()

