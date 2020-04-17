from setuptools import setup

setup(
    name='Tetrabot',
    version='1.0',
    packages=[],
    install_requires=[
        'numpy>=1.14.5',
        'tk',
        'Adafruit-Blinka',
        'Adafruit-PlatformDetect',
        'Adafruit-PureIO',
        'Pillow',
        'adafruit-circuitpython-busdevice',
        'adafruit-circuitpython-motor',
        'adafruit-circuitpython-pca9685',
        'adafruit-circuitpython-register',
        'adafruit-circuitpython-servokit',
        'cmake',
        'pyusb',
        'pyftdi',
        'pyserial',
        'setuptools'
    ],
    url='https://github.com/alexandrelafleur/Tetrabot',
    license='MIT',
    author='Tetrabot',
    author_email='',
    description='Quadriped Bot'
)
