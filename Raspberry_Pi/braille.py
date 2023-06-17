import RPi.GPIO as GPIO

MAX_BRAILLE_NO = 10

class Braille:
    def __init__(self, data_pin, latch_pin, clock_pin, no):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin
        self.braille_no = no
        self.data = [0]*MAX_BRAILLE_NO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(data_pin, GPIO.OUT)
        GPIO.setup(latch_pin, GPIO.OUT)
        GPIO.setup(clock_pin, GPIO.OUT)

    def on(self, no, index):
        self.data[self.braille_no - no - 1] |= (1 << index)

    def off(self, no, index):
        self.data[self.braille_no - no - 1] &= ~(1 << index)

    def refresh(self):
        GPIO.output(self.latch_pin, GPIO.LOW)
        for i in range(self.braille_no):
            self.shift_out(self.data_pin, self.clock_pin, self.data[i])
        GPIO.output(self.latch_pin, GPIO.HIGH)

    def all_off(self):
        for i in range(MAX_BRAILLE_NO):
            self.data[i] = 0

    @staticmethod
    def shift_out(data_pin, clock_pin, value):
        for i in range(8):
            GPIO.output(clock_pin, GPIO.LOW)
            GPIO.output(data_pin, (value & (1 << (7-i))) != 0)
            GPIO.output(clock_pin, GPIO.HIGH)
