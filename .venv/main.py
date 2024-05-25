import RPi.GPIO as GPIO
import time
import http.client
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
    try:
        print('1')
        connection = http.client.HTTPConnection(SERVER_HOST, SERVER_PORT)
        print('2')
        headers = {'Content-Type': 'text/plain'}
        print('3')
        connection.request('GET', '/', headers=headers)
        print('4')
    except e:
        print(e)
    finally:
        connection.close()

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=100)

try:

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
