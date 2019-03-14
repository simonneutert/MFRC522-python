#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import signal
import urllib2
import requests
import time

continue_reading = True

reader = SimpleMFRC522.SimpleMFRC522()

while continue_reading:

    try:
        id, text = reader.read()
        url = "http://localhost:8081/user/" + str(id)
        print(url)
        r = requests.post(url)
        print(r.content)
        print(id)
        print(text)
        time.sleep(5)
    finally:
        GPIO.cleanup()
