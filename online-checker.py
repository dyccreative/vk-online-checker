import requests
from bs4 import BeautifulSoup as bs
import time
import argparse
import subprocess

parser = argparse.ArgumentParser('python online-checker.py id123456789')
parser.add_argument('id', help='Paste here the user ID. ID format: id123456789 or other. !!!DO NOT PASTE A LINK!!!')
args = parser.parse_args()

online = ''

while online is not 'Online':

    r = requests.get('https://vk.com/' + args.id)
    html = bs(r.content, 'html.parser')
    online = html.select('.pp_last_activity_text')
    print(online[0].text)

    if online[0].text == 'Online':
        subprocess.call("termux-notification -c 'The user is Online!' --sound")
        break
    else:
        pass
    
    time.sleep(5)
