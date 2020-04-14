import requests
import threading
import colorama
from colorama import Fore,init
init()


tokens = []
def load_token():
    with open('check.txt', 'r') as f:   
        for x in f.readlines():
            tokens.append(x.replace('\n',''))

server = input('Server link: ')
def check():
    for x in tokens:
        s = requests.Session()
        api = 'https://discordapp.com/api/v6/invite/'+str((server))
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                "Authorization":x,
            }
        sender = s.post(api,headers=headers).text
        if "Unauthorized" in sender:
            print(Fore.RED+'[-] Invalid: '+x)
        else:
            if "You need to verify your account in order to perform this action." in sender:
                print(Fore.YELLOW+"[*] Verification required: "+x)
            else:
                print(Fore.GREEN+'[+] Valid: '+x)
                with open("valid.txt", "a") as save:
                    save.write(x+"\n")
load_token()     
check()
