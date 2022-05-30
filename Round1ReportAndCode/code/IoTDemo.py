from gpiozero import LED, Button
from signal import pause
from time import sleep
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
import socket

def sendDigit(no,serverIP,redled,greenled)
	d = json.dumps({"digit":no,"timestamp":datetime.now(),"serial":"U1234567890"})
	r = requests.post(serverIP+":"+serverPort,headers={"Content-Length":len(d)}data=d)
	data = json.loads(r.text())
	if data["success"] == '1':
		newled = redled
	elif data["success"] == '2':
		newled = greenled
	newled.on()
	sleep(1)
	newled.off()

#Wait for server to contact me 
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
jsonContent = json.loads(data)
serverIP = data["serverIP"]
serverPort = data["serverPort"]

print("UDP received")

redLED = LED(21)
greenLED = LED(20)

button = Button(23)
button2 = Button(24)

button.when_pressed = lambda : sendDigit(1,serverIP,redLED,greenLED)
button2.when_released = lambda : sendDigit(0,serverIP,redLED,greenLED)

pause()
