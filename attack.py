

import os
import sys
import time
import requests

def baha():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    print("\x1b[37;1mYour ID : "+id)
    
    httpCaht = requests.get("https://pastebin.com/mRqFXTH9").text
    if id in httpCaht:
        print("\x1b[37;1mYOUR ID IS ACTIVE.........")
        msg = str(os.geteuid())
        time.sleep(1)
        from lazyddos import hack
        hack()
            
    else:
        print("\x1b[37;1mYOUR ID IS NOT ACTIVE.........")
        time.sleep(1)
        sys.exit()


    if name == '__main__':
        baha()

os.system('xdg-open https://www.instagram.com/i.punjabii/')
os.system('clear')





baha()


         
hack()
