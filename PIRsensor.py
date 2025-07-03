This is the code for SunFounder Da Vinci Kit for Raspberry Pi. This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied wa rranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

davinci-kit-for-raspberry-pi comes with ABSOLUTELY NO WARRANTY; for details run ./show w. This is free software, and you are welcome to redistribute it under certain conditions; run ./show c for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program 'davinci-kit-for-raspberry-pi' (which makes passes at compilers).

Mike Huang, 21 August 2015

Mike Huang, Chief Executive Officer

Modified by ishi-0409, 2025

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
motion=18
LED=21
GPIO.setup(motion,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
sleep(10)
try:
    while True:
        motionval=GPIO.input(motion)
        print(motionval)
        if motionval==0:
            GPIO.output(LED,GPIO.LOW)
        if motionval==1:
            GPIO.output(LED,GPIO.HIGH)   
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
