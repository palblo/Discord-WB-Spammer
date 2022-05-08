from time import sleep
from colorama import Fore
from pystyle import Colorate, Colors, Write
from discord import Webhook, RequestsWebhookAdapter
import threading, requests

print(Colorate.Vertical(Colors.purple_to_red, '''

╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ┌─┐┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐
║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  └─┐├─┘├─┤││││││├┤ ├┬┘
╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  └─┘┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─ By Pąblo#4316

'''))

url = Write.Input(f"link -> ", Colors.red_to_purple, interval=0.00005)
message = Write.Input(f"message -> ", Colors.red_to_purple, interval=0.00005)
print()

def WebHook():
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    webhook.send(message)
    print(Colorate.Horizontal(Colors.red_to_purple, f"Sent MSG", 1))

while True:
    threading.Thread(target=WebHook).start()

