import time
import board
import busio

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from relay import Relay

class Garden:
  PIN_NUMBERS = [31, 33, 35, 37]

  ads = None
  channels = []
  relays = []

  def __init__(self, i2c):
    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    # Create single-ended input on each channel
    for x in range(0, 4):
      channel_no = 'P%s' % x
      channel_name = getattr(ADS, channel_no)
      # channel.value, channel.voltage
      channel = AnalogIn(ads, channel_name)
      self.channels.append(channel)

    for pin in self.PIN_NUMBERS:
      self.channels.append(Relay(pin))