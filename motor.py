from machine import I2C, Pin

_MotorSpeedSet    = 0x82
_PWMFrequenceSet  = 0x84
_DirectionSet     = 0xaa
_MotorSetA        = 0xa1
_MotorSetB        = 0xa5
_Nothing          = 0x01
_EnableStepper    = 0x1a
_UnenableStepper  = 0x1b
_Stepernu         = 0x1c

class Motor:

    def __init__(self, i2c=None, address=0x0F):
        self._i2c = i2c
        if i2c is None:
            self._i2c = I2C(sda=Pin(21), scl=Pin(22))
            
        self._address = address
        
    def _writeto(self, mem, data):
        print("writeto: ", self._address, data)
        self._i2c.writeto_mem(self._address, mem, bytearray(data))
        
    def setDirection(self, direction):
        self._writeto(_DirectionSet, [direction, _Nothing])
        
    def setMotorSpeed(self, motorA, motorB):
        self._writeto(_MotorSpeedSet, [motorA, motorB])
        
