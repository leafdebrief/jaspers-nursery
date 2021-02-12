# Jasper's Nursery

**Jasper's Nursery** is a Python library for controlling the eponymous Raspberry Pi HAT garden controller and monitor.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `jaspers-nursery`:

```bash
pip3 install jaspers-nursery
```

## Usage

```python
import time
import board
import busio
import jaspers_nursery

i2c = busio.I2C(board.SCL, board.SDA)
garden = jaspers_nursery.Garden(i2c)

# read analog channel
a0value = garden.channels[0].value
a0voltage = garden.channels[0].voltage

print(a0value, a0voltage)
# >>> 808 1.61679

# control relays manually
garden.relays[0].on()
time.sleep(1)
garden.relays[0].off()

# or toggle one on and off
relay0 = garden.relays[0]
relay0.toggle()
time.sleep(1)
relay0.toggle()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)