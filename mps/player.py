import os,sys,time,keyboard
import subprocess
from mps_pkg import *

search = 'arijit singh'

#os.system(' echo ".%s"; sleep 2; echo "all" | mps' % search)
#os.system('echo "all" | mps')
#child = subprocess.Popen('mps', stdin=subprocess.PIPE)
#child.communicate('.linkin park')

list = main.search(search)
list = main.generate_songlist_display()
while True:
    main.play_all(list,search)
    time.sleep(5)
    keyboard.press('enter')
