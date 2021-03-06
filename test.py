#!/usr/bin/env python
#
# GrovePi Example for using the Grove - Temperature&Humidity Sensor (High-Accuracy & Mini)(http://www.seeedstudio.com/depot/Grove-TemperatureHumidity-Sensor-HighAccuracy-Mini-p-1921.html
#		
# This example prints the gesture on the screen when a user does an action over the sensor
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
#################################################################################################################################################
# NOTE:
# The software for this sensor is still in development and might make your GrovePi unuable as long as this sensor is connected with the GrovePi
#################################################################################################################################################
from I2C_TempHum_Sensor import I2C_temp_hum_mini
from I2C_Barometer_Sensor import hp206c
import time


h= hp206c.hp206c()
t= I2C_temp_hum_mini.th02()

ret=h.isAvailable()
if h.OK_HP20X_DEV == ret:
    print("HP20x_dev is available.")
else:
    print("HP20x_dev isn't available.")
    
temp=h.ReadTemperature()
pressure=h.ReadPressure()
altitude=h.ReadAltitude()

while True:
    print("Temp: %.2fC\tHumidity:%.2f" %(t.getTemperature(),t.getHumidity()),"%") 
    print("Temperature\t: %.2f C\nPressure\t: %.2f hPa\nAltitude\t: %.2f m" %(temp,pressure,altitude))
    time.sleep(5)