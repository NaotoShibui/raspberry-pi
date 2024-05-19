import RPi.GPIO as GPIO
import time
import socket

# サーバーのIPアドレスとポート番号
SERVER_HOST = os.getenv('SERVER_HOST')  # 環境変数からサーバーのIPアドレスを取得
if not SERVER_HOST:
    raise ValueError("環境変数 'SERVER_HOST' が設定されていません")
SERVER_PORT = 3000

# GPIOピンの設定
BUTTON_PIN = 4

# GPIOの初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# タクトスイッチの状態を監視し、ONになったときにTCP通信を行う関数
def button_callback(channel):
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        print('タクトスイッチがONになりました。')
        send_message()

# TCP通信でメッセージを送信する関数
def send_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(b'タクトスイッチがONになりました。')
        data = s.recv(1024)
        print('受信データ:', data.decode())

# イベント検出の設定
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=100)

try:
    # プログラムを終了せずに待機
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # プログラム終了時にGPIOのリソースを解放
    GPIO.cleanup()
