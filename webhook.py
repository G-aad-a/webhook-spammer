import string
import random
import time
import requests
import json
from colorama import init, Fore
init()



def mainelars():
    print(Fore.GREEN + '[+] Enter The Webhook Link: ')
    webhook = input()
    print('[+] Enter The Message: ')
    message = input()
    try:
        while True:
            try:
                time.sleep(0.1)
                data = requests.post(webhook, json={'content': message})
                if  data.status_code == 204:
                    print("[+] Sendte ==> [" + message + "]") 
            except:
                print("Error i webhooken")
                time.sleep(5)
                quit()
    except KeyboardInterrupt:
        print("Bye..")
        quit()

if __name__ == "__main__":
    mainelars()