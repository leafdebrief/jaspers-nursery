from setuptools import find_packages, setup

setup(
  name='jaspers-nursery',
  packages=find_packages(include=['jaspers-nursery']),
  version='0.1.0',
  description='Python library for controlling the eponymous Raspberry Pi HAT garden controller and monitor',
  author='Jasper Fulowitz',
  license='MIT',
  install_requires=['python3-rpi.gpio', 'adafruit-blinka', 'adafruit-circuitpython-ads1x15',]
)