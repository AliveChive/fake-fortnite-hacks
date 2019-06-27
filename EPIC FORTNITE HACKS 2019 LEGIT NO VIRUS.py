import os
import webbrowser
import time
import requests

clear = lambda: os.system('cls')

ip = requests.get('http://checkip.dyndns.org/').text
ip = ip = ip[76:].replace('</body></html>','').rstrip()

for x in range(int(2)):
    print ('loading epic hacks.')
    time.sleep(.5)
    clear()
    print ('loading epic hacks..')
    time.sleep(.5)
    clear()
    print ('loading epic hacks...')
    time.sleep(.5)
    clear()
webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

while True:
    print('ur ip is ' + ip + ' lmaoooo')
