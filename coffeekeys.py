import os
from time import sleep

os.system ('clear')

print('  ╰╮╰╮╰╮')
sleep(0.05)
print(' ╭━━━━━━━╮╱ ')
sleep(0.05)
print(' ╰━━━━━━━╯╱ ')
sleep(0.05)
print(' ┃╭╭╮┏┏┏┏┣━╮ ')
sleep(0.05)
print(' ┃┃┃┃┣┣┣┣┃╱┃ ')
sleep(0.05)
print(' ┃╰╰╯┃┃┗┗┣━╯ ')
sleep(0.05)
print(' ╰━━━━━━━╯ ')
sleep(0.05)
print(' COFFEEKEYS ')
sleep(0.05)

print('   [y/n]')
text1 = input('︻╦╤─ ')
if text1  == 'y':
  print('  ■□□□□20%')
  sleep(0.25)
  print('  ■■□□□40%')
  sleep(0.50)
  print('  ■■■□□60%')
  sleep(0.75)
  print('  ■■■■□80%')
  sleep(1)
  print('  ■■■■■100%')
  sleep(1.25) 

  try:
         os.mkdir('/data/data/com.termux/files/home/.termux')
  except:
         pass

  konci = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
  kunci = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
  kunci.write(konci)
  kunci.close()
  sleep(0.50)
  os.system('termux-reload-settings')
  print('[!] SUCCESSFULL:)')
  sleep(0.50)

else:
  print('NOT IN INSTALL')
