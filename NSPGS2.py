# Author: Benjamin Janzen Feb 2023
#
# This module borrows from the Libraries below (from Adafruit and that of Paul Cunnane and Peter Dahelbrg)
# Original Copyright notices are reproduced below
#
#
# Authors: Paul Cunnane 2016, Peter Dahlebrg 2016
#
# This module borrows from the Adafruit BME280 Python library. Original
# Copyright notices are reproduced below.
#
# Those libraries were written for the Raspberry Pi. This modification is
# intended for the MicroPython and esp8266 boards.
#
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Based on the BMP280 driver with BME280 changes provided by
# David J Taylor, Edinburgh (www.satsignal.eu)
#
# Based on Adafruit_I2C.py created by Kevin Townsend.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import time
from ustruct import unpack, unpack_from
from array import array

# NSPGS2_D default address.
NSPGS2_I2CADDR = 0x7F
#NSPGS2_I2CADDR_R = 0xFF


class NSPGS2:

    def __init__(self,
                 address=NSPGS2_I2CADDR,
                 i2c=None,
                 **kwargs):
        # Check i2c
        self.address = address
        ##self.raddress = raddress
        if i2c is None:
            raise ValueError('An I2C object is required.')
        self.i2c = i2c

        
        # temporary data holders which stay allocated
        self._initdata_barray = bytearray(1)
        self._l1_barray = bytearray(1)
        self._raw_barray = bytearray(3)
        self._l3_resultarray = array("i", [0])

    def read_raw_data(self, result=None):
        """ Reads the raw (uncompensated) data from the sensor.

            Args:
                result: array of length 3 or alike where the result will be
                stored, in temperature, pressure, humidity order
            Returns:
                None
        """

        #Write data 0x0A into register 0x30 with universal address NSPGS2_I2CADDR_R   
        self._initdata_barray[0] = 0x0A
        self.i2c.writeto_mem(self.address, 0x30, self._initdata_barray, addrsize=8)
        
        time.sleep_ms(3)  # Wait the required time

        # readout pressure measurement data from 0x06 to 0x08
        self.i2c.readfrom_mem_into(self.address, 0x06, self._raw_barray)
        readout = self._raw_barray
        
        rawdata = ((readout[0] << 16) | (readout[1] << 8) | readout[2])
        
        result = rawdata
        return result
    
        return array("i", (result))

    
    @property
    def values(self):
        """ human readable values """
        
        pCode = self.read_raw_data()
        
        p = (pCode / 8388607 - 0.1) / 0.0160
        
        #str(p)
        
        #print("{:.5f} kPA".format(p))
                
        return ("{:.4}kPa".format(p))
        
