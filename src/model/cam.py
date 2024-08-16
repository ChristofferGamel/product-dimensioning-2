import time
from picamera2 import Picamera2
import cv2
import numpy as np

class Picture():
    def __init__(self) -> None:
        pass

    def picture(self, cam):

        picam = Picamera2(camera_num=cam)
        controls = {"ExposureTime": 1600, 
                    "AnalogueGain": 1.2, 
                    "Brightness": 0.08,
                    "Sharpness":3,
                    "AwbMode":5
                    }
        config = picam.create_preview_configuration(main={"size": (1152, 648)}, controls=controls)
        picam.configure(config)

        
        picam.start()
        time.sleep(1)

        org_image = picam.capture_image()
        picam.close()

        opencv_image = cv2.cvtColor(np.array(org_image), cv2.COLOR_RGBA2BGR)
        print(opencv_image)
        return opencv_image
    
if __name__ == "__main__":
    pic = Picture()
    pic.picture(0)

