import requests
import os

def get_ip_info():
    os.system('clear')
    print("====================================")
    print("      IP FINDER BY RANA.NJ")
    print("====================================\n")
    
    ip = input("[+] Enter IP Address (Leave blank for yours): ")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n[!] IP Address: {data['query']}")
            print(f"[!] Country:    {data['country']}")
            print(f"[!] City:       {data['city']}")
            print(f"[!] ISP:        {data['isp']}")
        else:
            print("\n[-] Invalid IP Address!")
    except:
        print("\n[-] Connection Error!")

if __name__ == "__main__":
    get_ip_info()
