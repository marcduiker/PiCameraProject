import fractions

class CameraSettings:
    """ CameraSettings class to control the Pi Camera"""
    def __init__(self):
        self._isautomatic = True
        self._iso = 400
        self._whitebalance = 'auto'
        self._shutterspeed = 0.01
        self._framerate = fractions.Fraction(1, 50)

    @property
    def isautomatic(self):
        return self._isautomatic

    @isautomatic.setter
    def isautomatic(self, value):
        self._isautomatic = value

    @property
    def iso(self):
        return self._iso
    
    @iso.setter
    def iso(self, value):
        self._iso = value

    @property
    def framerate(self):
        return self._framerate
    
    @framerate.setter
    def framerate(self, value):
        self._framerate = fractions.Fraction(1, value)

    @property
    def whitebalance(self):
        return self._whitebalance
    
    @whitebalance.setter
    def whitebalance(self, value):
        self._whitebalance = value

    @property
    def shutterspeed(self):
        return self._shutterspeed
    
    @shutterspeed.setter
    def shutterspeed(self, value):
        self._shutterspeed = value * 1000000
