from pystyle import Colorate, Colors, Write      
import requests                                  
from threading import Thread                     
from time import sleep

print(Colorate.Horizontal(Colors.purple_to_red, '''

┬ ┬┌─┐┌┐ ┬ ┬┌─┐┌─┐┬┌─  ┌─┐┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐ 
│││├┤ ├┴┐├─┤│ ││ │├┴┐  └─┐├─┘├─┤││││││├┤ ├┬┘
└┴┘└─┘└─┘┴ ┴└─┘└─┘┴ ┴  └─┘┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─ By Pąblo#4316

Pąblo#4316 | https://github.com/palblo/SpotifyGen
'''))
9*
print(Colorate.Horizontal(Colors.red_to_white, '''
VERSION: V1.2
NOTE : the message counter may not be accurate

'''))

url = Write.Input(f"\nlink -> ", Colors.red_to_purple, interval=0.00005)
message = Write.Input(f"message -> ", Colors.red_to_purple, interval=0.00005)
print()

data = {
    "content": message,
    "username": "SPAMMER_V1.2"
}

count = 0

def WebHook():
    global count
    r = requests.post(url, data=data)
    if r.status_code == 204:
        messagescount = (Colorate.Horizontal(Colors.red_to_purple, f"Messages : {count}", 1))
        messages = print(messagescount, end='\r')
        count += 1

while True:
    Thread(target=WebHook).start()
