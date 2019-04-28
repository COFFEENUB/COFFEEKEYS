import os
from time import sleep

os.system ('clear')

print('  ╰╮╰╮╰╮')
print(' ╭━━━━━━━╮╱ ')
print(' ╰━━━━━━━╯╱ ')
print(' ┃╭╭╮┏┏┏┏┣━╮ ')
print(' ┃┃┃┃┣┣┣┣┃╱┃ ')
print(' ┃╰╰╯┃┃┗┗┣━╯ ')
print(' ╰━━━━━━━╯ ')
print(' COFFEEKEYS ')

try:
       os.mkdir('/data/data/com.termux/files/home/.termux')
except:
       pass

print('[!] MAKING FILE')
sleep(2)
konci = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kunci = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kunci.write(konci)
kunci.close()
print('[!] SETTINGS UP')
sleep(2)
os.system('termux-reload-settings')
print('[!] SUCCESSFULL:)')
sleep(2)
