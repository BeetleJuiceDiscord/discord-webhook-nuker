import os
import requests
from dhooks import Webhook
import time

os.system("title Discord Webhook Nuker")

def banner():
    print("""

Discord Webhook Nuker | By King Herod

        Input Webhook URL

    """)

def nuker():
    start = input(">")
    hook = Webhook(start)
    hook.send("This webhook has forcefully been deleted :gorilla: :middle_finger: :gorilla:")
    x = requests.delete(start)

def end():
    print("Successfully nuked webhook\n")
    print("Closing in 10 seconds...")
    time.sleep(10)
    os.system("exit")


banner()
nuker()
end()
