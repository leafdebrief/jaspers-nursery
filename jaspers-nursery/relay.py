import RPi.GPIO as GPIO

class Relay:
  def __init__(self, pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    self.pin = pin
    self.state = False

  def on(self):
    GPIO.output(self.pin, 1)
    self.state = True

  def off(self):
    GPIO.output(self.pin, 0)
    self.state = False

  def toggle(self):
    if self.state:
      GPIO.output(self.pin, 1)
    else:
      GPIO.output(self.pin, 0)
    
    self.state = !self.state
