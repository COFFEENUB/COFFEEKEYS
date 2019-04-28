import os
from time import sleep

os.system('clear')

print('╰╮╰╮╰╮')
sleep(0.05)
print('╭━━━━━━━╮╱')
sleep(0.05)
print('╰━━━━━━━╯╱')
sleep(0.05)
print('┃╭╭╮┏┏┏┏┣━╮')
sleep(0.05)
print('┃┃┃┃┣┣┣┣┃╱┃')
sleep(0.05)
print('┃╰╰╯┃┃┗┗┣━╯')
sleep(0.05)
print('╰━━━━━━━╯')
sleep(0.05)
print('COFFEEKEYS')
sleep(0.05)

text1 = input('Do you want to continue? [Y/n] ')
if text1  == 'y':

  os.system ('clear')

  print('    PROCESSING')
  print('__________________')
  print('     ■□□□□20%')
  sleep(0.25)
  print('     ■■□□□40%')
  sleep(0.50)
  print('     ■■■□□60%')
  sleep(0.75)
  print('     ■■■■□80%')
  sleep(1)
  print('     ■■■■■100%')
  sleep(1.25)

  try:
         os.mkdir('/data/data/com.termux/files/home/.termux')
  except:
         pass

  text_ = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
  _text = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
  _text.write(text_)
  _text.close()
  os.system('termux-reload-settings')
  print(' [!] SUCCESSFULL')
  sleep(0.50)

if text1  == 'Y':

  os.system ('clear')

  print('    PROCESSING')
  print('__________________')
  print('     ■□□□□20%')
  sleep(0.25)
  print('     ■■□□□40%')
  sleep(0.50)
  print('     ■■■□□60%')
  sleep(0.75)
  print('     ■■■■□80%')
  sleep(1)
  print('     ■■■■■100%')
  sleep(1.025)

  try:
         os.mkdir('/data/data/com.termux/files/home/.termux')
  except:
         pass

  text_ = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
  _text = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
  _text.write(text_)
  _text.close()
  os.system('termux-reload-settings')
  print(' [!] SUCCESSFULL')
  sleep(0.50)
