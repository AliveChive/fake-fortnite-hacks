import os
import webbrowser
import time
import requests

clear = lambda: os.system('cls')

ip = requests.get('https://api.ipify.org').text

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
