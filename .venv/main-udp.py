import RPi.GPIO as GPIO
import time
import socket
import os

SERVER_HOST = os.getenv('SERVER_HOST') 
SERVER_PORT = 3000
BUTTON_PIN = 4

print(SERVER_HOST)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        print('switch ON')
        send_message()

def send_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.sendto('switch ON'.encode(), (SERVER_HOST, SERVER_PORT))
        
    finally:
        s.close()

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=100)

try:

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
