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
    # Simple and Error-free Banner
    print(f"""
{R}   R R R     A     N   N    A
{R}   R   R    A A    NN  N   A A
{Y}   R R R   A   A   N N N  A   A
{Y}   R R    AAAAAAA  N  NN AAAAAAA
{G}   R  R   A     A  N   N A     A  {W}IP FINDER
{C}   ====================================
           CREATED BY: RANA.NJ
   ====================================
    """)

def get_ip_info():
    banner()
    ip = input(f"{Y}Enter Target IP (or leave blank for yours): {W}")
    print(f"\n{C}[*] Fetching details...{W}")
    time.sleep(1)
    
    try:
        # Using a reliable IP API
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{G}[+] IP Address : {W}{data['query']}")
            print(f"{G}[+] Country    : {W}{data['country']}")
            print(f"{G}[+] City       : {W}{data['city']}")
            print(f"{G}[+] ISP        : {W}{data['isp']}")
            print(f"{G}[+] Zip Code   : {W}{data['zip']}")
        else:
            print(f"\n{R}[!] Error: Invalid IP or Private IP!{W}")
    except Exception as e:
        print(f"\n{R}[!] Connection Error! Make sure internet is on.{W}")

if __name__ == "__main__":
    get_ip_info()
