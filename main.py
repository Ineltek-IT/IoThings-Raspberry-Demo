from machine import Pin, I2C
import rp2
import utime as time
import NSPGS2
import tm1637


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

tm = tm1637.TM1637(clk=Pin(21), dio=Pin(20))

val_max = 0

while True:
    
#Read sensor data
    sensor_reading = NSPGS2.NSPGS2(i2c=i2c)
    pressure = float(sensor_reading.values[:-3])
    if(pressure>val_max):
        val_max=pressure
    print(str(val_max))
    print('Pressure = {}'.format(str(pressure)))
    tm.number(int(pressure*1000))

    
#delay 5 seconds
    time.sleep(0.5)
