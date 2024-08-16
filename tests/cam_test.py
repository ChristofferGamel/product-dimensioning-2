import time
from picamera2 import Picamera2
from gpiozero import LED

class Picture():       
    def picture(self, filename, cam):
        led = LED(14)
        picam0 = Picamera2(camera_num=0)
        picam1 = Picamera2(camera_num=1)
        controls = {"AnalogueGain": 1.2, 
                    "Brightness": 0.08,
                    "Sharpness":3,
                    "AwbMode":5
                    }
        config = picam0.create_preview_configuration(main={"size": (int(2304*0.75), int(1296*0.75))}, controls=controls)
        config = picam1.create_preview_configuration(main={"size": (int(2304*0.75), int(1296*0.75))}, controls=controls)
        picam0.configure(config)
        picam1.configure(config)

        led.on()
        time.sleep(0)

        picam0.start()
        picam1.start()

        picam0.capture_file("cam0.jpg")
        picam1.capture_file("cam1.jpg")

        picam0.close()
        picam1.close()

        led.off()

start = time.time()

picture_taker = Picture()
picture_taker.picture("cam0.jpg", 0)

end = time.time()
print("Time: ", end-start)