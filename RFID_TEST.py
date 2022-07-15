
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time


while True:
        reader = SimpleMFRC522()
        try:
                id, text = reader.read()
                if id:
                        print(id)
                        time.sleep(1)
        finally:
                GPIO.cleanup()