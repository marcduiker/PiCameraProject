class CameraSettings:
    """ CameraSettings class to control the Pi Camera"""
    def __init__(self):
        self._exposuremode = 'auto'
        self._isautomatic = True
        self._iso = 400
        self._whitebalance = 'auto'
        self._shutterspeed = 0.01
        self._framerate = 30

    @property
    def exposuremode(self):
        return self._exposuremode

    @exposuremode.setter
    def exposuremode(self, value):
        self._exposuremode = value

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
        self._framerate = value

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
