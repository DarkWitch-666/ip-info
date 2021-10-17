#PYTHON 3
import urllib.request
import json
import http.client
import os
import random
import bs4
import socket
import time
import requests #!
import sys
from colorama import Fore #!
from bs4 import BeautifulSoup as BS #!

RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'

def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

if not checkInternetSocket():

    sys.exit("internet connection failed...")
    time.sleep(3)
print( "-" * 45 )
system = input(f" Enter your system\n Linux/Termux - 1\n Windows - 2\n -> ")
print( "-" * 45 )
if system == '1':
	try:
		os.system("clear")
	except:
		sys.exit("error")
if system == '2':
	try:
		os.system("cls")
	except:
		sys.exit("error")
example_ip = ['188.165.90.184', '172.217.169.142', '66.254.114.41 ', '140.82.113.3 ', '104.26.10.147']
print(f"""{Fore.YELLOW}
	.                                            .
 	██╗██████╗░░░░░░░██╗███╗░░██╗███████╗░█████╗░
 	██║██╔══██╗░░░░░░██║████╗░██║██╔════╝██╔══██╗
 	██║██████╔╝█████╗██║██╔██╗██║█████╗░░██║░░██║
 	██║██╔═══╝░╚════╝██║██║╚████║██╔══╝░░██║░░██║
 	██║██║░░░░░░░░░░░██║██║░╚███║██║░░░░░╚█████╔╝
 	╚═╝╚═╝░░░░░░░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
	.                                            .
""")    
print(f"{RED}		By >> .:lukas:.\n")
print(f"{Fore.GREEN}		Example ip >> {random.choice(example_ip)}")
getIP = input(f"{GREEN}  {socket.gethostname()}@ip-info ~{RED} ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen( url )

except:
    print()
    sys.exit( f"\n 			{RED}UNKNOW IP!				" )

ipINFO = json.load(getInfo)

def whoisIPinfo(ip):

    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo

    except:

        return "\n [×_ ×] — ERROR — [× _×] \n"

     
print( RED + "-" * 60 )
try:
	print( f"{GREEN} IP - ", ipINFO["ip"] )
	print( " CITY - ", ipINFO["city"] )
	print( " REGION - ", ipINFO["region"] )
	print( " COUNTRY - ", ipINFO["country"] )
	print( " LOC - ", ipINFO["loc"] )
	print( " ORG - ", ipINFO["org"] )
	print( " TIME ZONE - ", ipINFO["timezone"] )
	print( RED + "-" * 60 )
	#pzdc = ['little-known providers work only in \ntwo or three cities or regions.\nso look sometimes for information about providers.\nthis way de-anonymization will be easier!',
	 #'prepare a new fresh proxy before going internet!', 'different ip do not always have accurate information!', 
	 #'to find out the ip address of a person without\nhaving access to his wifi.\njust use> iplogger.com']
	#print('random advice:')
	#print(GREEN + random.choice(pzdc))
	#print( RED + "-" * 60 )
except:
	print("[×_ ×] — ERROR — [× _×]")

print(f"{RED}\nPress 'enter' to exit")
input()