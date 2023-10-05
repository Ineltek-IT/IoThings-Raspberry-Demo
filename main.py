from machine import Pin, I2C
import rp2
import utime as time
import NSPGS2


# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)

#initialise I2C
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

time.sleep_ms(100)

carray = bytearray(1)
#Check I2C communication
i2c.readfrom_mem_into(0x7F, 0x6c, carray, addrsize=8)

time.sleep_ms(100)

print('Reg 0x6c is', carray)


while True:
    
#Read sensor data
    sensor_reading = NSPGS2.NSPGS2(i2c=i2c)
    pressure = sensor_reading.values
    print('Pressue = {}'.format(pressure))
    
#delay 5 seconds
    time.sleep(1)
