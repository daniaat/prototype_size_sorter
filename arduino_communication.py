''''
Author: MOstafa elkabir & Taha Anwar
company: Daniaat
project: Size Sorter

this file have functions to communicate with the arduino

'''

#!/usr/bin/env python
import serial
import string
import time


def init_connection():
    connection = serial.Serial("/dev/ttyAMA0", 9600)
    connection.open()
    return connection

def send_to_arduino(coneection, command):

    try:
        while True:
            coneection.write(string(command))

    except KeyboardInterrupt:
        pass  # do cleanup here
    pass

def tell_arduino_to_recive(connection,command):
  connection.flushInput()
  connection.flushOutput()
  connection.write(command)
  while True:
    try:
      time.sleep(0.01)
      flag = connection.readline()
      print flag
      return flag
    except:
      pass

def close_connection(connection):
    connection.close()
