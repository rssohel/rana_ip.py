import requests
import os
import time

# Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[0m'

def banner():
    os.system('clear')
    # Logo for Rana IP Finder
    print(fr"""
{R}   _____ _____    {Y} ______ _           _
{R}  |_   _|  __ \   {Y}|  ____(_)         | |
{R}    | | | |__) |  {Y}| |__   _ _ __   __| | ___ _ __
{R}    | | |  ___/   {Y}|  __| | | '_ \ / _` |/ _ \ '__|
{R}   _| |_| |       {Y}| |    | | | | | (_| |  __/ |
{R}  |_____|_|       {Y}|_|    |_|_| |_|\__,_|\___|_|
{C}
       >> CREATED BY: RANA.NJ <<
    ====================================
    """)

def get_ip_info():
    banner()
    ip = input(f"{Y}Enter Target IP (or leave blank for yours): {W}")
    print(f"\n{C}[*] Fetching details...{W}")
    time.sleep(1.5)
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{G}[+] IP Address : {W}{data['query']}")
            print(f"{G}[+] Country    : {W}{data['country']} ({data['countryCode']})")
            print(f"{G}[+] City       : {W}{data['city']}")
            print(f"{G}[+] ISP        : {W}{data['isp']}")
            print(f"{G}[+] Org        : {W}{data['org']}")
            print(f"{G}[+] Timezone   : {W}{data['timezone']}")
        else:
            print(f"\n{R}[!] Error: Invalid IP Address!{W}")
    except:
        print(f"\n{R}[!] Connection Error! Check internet.{W}")

if __name__ == "__main__":
    get_ip_info()
    cd $HOME && rm -rf rana-ip-finder && git clone https://github.com/rssohel/rana-ip-finder && cd rana-ip-finder && python rana_ip.py
