from gpiozero import LED

class Lights():
    def __init__(self) -> None:
        self.led = LED(14)

    def off(self):
        self.led.off()

    def on(self):
        self.led.on()