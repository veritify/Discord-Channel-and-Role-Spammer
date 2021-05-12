import sys
import ctypes
import json
import string
import random
from os import system
from random import randint
from itertools import cycle
from time import time, sleep
from threading import Thread
from pypresence import Presence
import requests_futures.sessions
from requests_futures.sessions import FuturesSession
import requests
version = "1.0"
ctypes.windll.kernel32.SetConsoleTitleW("Veritify's Tool")
session = FuturesSession()
user_ids = []
role_ids = []
channel_ids = []
proxies = []
rotating = cycle(proxies)

if sys.platform == "linux":
    clear = lambda: system("clear")
else:
    clear = lambda: system("cls & mode 80,24")

clear()
print('''
     \x1b[38;5;199m    __                     

██╗░░░██╗███████╗██████╗░██╗████████╗██╗███████╗██╗░░░██╗
██║░░░██║██╔════╝██╔══██╗██║╚══██╔══╝██║██╔════╝╚██╗░██╔╝
╚██╗░██╔╝█████╗░░██████╔╝██║░░░██║░░░██║█████╗░░░╚████╔╝░
░╚████╔╝░██╔══╝░░██╔══██╗██║░░░██║░░░██║██╔══╝░░░░╚██╔╝░░
░░╚██╔╝░░███████╗██║░░██║██║░░░██║░░░██║██║░░░░░░░░██║░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝░░░░░░░░╚═╝░░░\x1b[0m\x1b[0mVeritify#0001
''')

try:
    for line in open('Proxies.txt'):
        proxies.append(line.replace('\n', ''))
except:
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFailed To Load Proxies From Proxies.txt")

with open('Config.json') as f:
    config = json.load(f)

role = config.get('rolespam')
channelname = config.get('channelspam')
channel = config.get('channelspamid')
spam = config.get('spam_message')
Token = config.get('Token')
Bot = config.get('Bot')
guild = config.get('guild-id')
if Bot == True:
    headers = {"Authorization": f"Bot {Token}"}
else:
    headers = {"Authorization": f"{Token}"}

class LunaMisc:

    
    def Check(token, bot):
        if bot == True:
            headers = {"Authorization": f"Bot {token}"}
        else:
            headers = {"Authorization": f"{token}"}
        r = session.get("https://discord.com/api/v8/users/@me", headers=headers).result()
        if r.status_code == 200:
            return True
        else:
            return False


    def Create_Channel(guild_id):
        try:
            name = channelname
            json = {'name': name, 'type': 0}
            r = session.post(f'https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/channels', headers=headers, json=json, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Created Channel {r.json()['id']}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Create_Channel, args=(guild_id,)).start()
        except:
            pass

    def Create_Role(guild_id):
        try:
            name = role
            json = {'name': name}
            r = session.post(f'https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/roles', headers=headers, json=json, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Created Role {r.json()['id']}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Create_Role, args=(guild_id,)).start()
        except:
            pass
            


def Init():
    if LunaMisc.Check(Token, Bot):
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mToken: \n               " + Token)
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mGuild ID: {guild}")
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mChannel ID for spam: {config.get('channelspamid')}")
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mMessage to spam: {config.get('spam_message')}")
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mName of channel to spam: {config.get('channelspam')}")
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mName of role to spam: {config.get('rolespam')}")


        
        try:
            members = open('Scraped/Members.txt').readlines()
            for member in members:
                member = member.replace("\n", "")
                user_ids.append(member)

            roles = open('Scraped/Roles.txt').readlines()
            for role in roles:
                role = role.replace("\n", "")
                role_ids.append(role)

            channels = open('Scraped/Channels.txt').readlines()
            for channel in channels:
                channel = channel.replace("\n", "")
                channel_ids.append(channel)
        except:
            print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFailed To Load Scraped Data!")


        sleep(2)
        Menu(guild)
    else:
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mYour Token Is Invalid")
        input()
        exit()

def Menu(guild):
	try:
	    clear()
	    print('''
     \x1b[38;5;199m    __                     
       
██╗░░░██╗███████╗██████╗░██╗████████╗██╗███████╗██╗░░░██╗
██║░░░██║██╔════╝██╔══██╗██║╚══██╔══╝██║██╔════╝╚██╗░██╔╝
╚██╗░██╔╝█████╗░░██████╔╝██║░░░██║░░░██║█████╗░░░╚████╔╝░
░╚████╔╝░██╔══╝░░██╔══██╗██║░░░██║░░░██║██╔══╝░░░░╚██╔╝░░
░░╚██╔╝░░███████╗██║░░██║██║░░░██║░░░██║██║░░░░░░░░██║░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝░░░░░░░░╚═╝░░░ \x1b[0mEARLY BETA\x1b[0m

     \x1b[38;5;199m[\x1b[0m1\x1b[38;5;199m] \x1b[0mCreate Channels
     \x1b[38;5;199m[\x1b[0m2\x1b[38;5;199m] \x1b[0mCreate Roles
     \x1b[38;5;199m[\x1b[0m3\x1b[38;5;199m] \x1b[0mSpam Channel
	    ''')
	    opt = input(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mOption\x1b[38;5;199m: \x1b[0m")
#	    if opt == "1":
#	        for i in range(len(user_ids)):
#	            Thread(target=LunaMisc.Ban, args=(guild, user_ids[i],)).start()
#	        sleep(2)
#	        Menu(guild)
#	    elif opt == "2":
	#        for i in range(len(user_ids)):
#	            Thread(target=LunaMisc.Kick, args=(guild, user_ids[i],)).start()
	#        sleep(2)
	#        Menu(guild)
	    #elif opt == "3":
	     #   for i in range(len(user_ids)):
	      #      Thread(target=LunaMisc.Unban, args=(guild, user_ids[i],)).start()
	       # sleep(2)
	        #Menu(guild)
	    #elif opt == "4":
	   #     for i in range(len(role_ids)):
	    #        Thread(target=LunaMisc.Delete_Role, args=(guild, role_ids[i],)).start()
	     #   sleep(2)
	      #  Menu(guild)

	    if opt == "1":
	        for i in range(100):
	            Thread(target=LunaMisc.Create_Channel, args=(guild,)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "2":
	        for i in range(100):
	            Thread(target=LunaMisc.Create_Role, args=(guild,)).start()
	        sleep(2)
	        Menu(guild)
	    else:
	        Init()
	except:
		pass


if __name__ == "__main__":
    Init()