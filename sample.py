from m5stack import lcd
from machine import I2C, Pin
from motor import Motor
from time import sleep_ms

lcd.clear()
lcd.setCursor(0, 0)
lcd.setColor(lcd.WHITE)
lcd.print("Hello World!")

i2c = I2C(scl=Pin(22), sda=Pin(21))

m = Motor(i2c = i2c, address = 0x0F)

while True:
    m.setMotorSpeed(100, 100)
    m.setDirection(0b0000)
    sleep_ms(1000)
    m.setDirection(0b0101)
    sleep_ms(1000)
    m.setDirection(0b1010)
    sleep_ms(1000)
    m.setDirection(0b1111)
    sleep_ms(1000)

