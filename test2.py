#import argparse
import subprocess
import shutil
import time
from datetime import datetime

from bluepy.btle import BTLEDisconnectError
from cursesmenu import *
from cursesmenu.items import *

from constants import MUSICSTATE
from miband import miband

MAC_ADDR = 'DE:97:B3:D6:72:72'
AUTH_KEY = '6f2e50d358d8f63c54559979a5d9d342'

# Convert Auth Key from hex to byte format
if AUTH_KEY:
    AUTH_KEY = bytes.fromhex(AUTH_KEY)

def send_notif(msg):
    #title = input ("Enter title or phone number to be displayed: ")
    #print ('Reminder: at Mi Band 4 you have 10 characters per line, and up to 6 lines. To add a new line use new line character \n')
    #msg = input ("Enter optional message to be displayed: ")
    #ty= int(input ("1 for Mail / 2 for Message / 3 for Missed Call / 4 for Call: "))
    
    title = 'message'
    ty = 1

    if(ty > 4 or ty < 1):
        print ('Invalid choice')
        time.sleep(2)
        return
    a=[1,5,4,3]
    band.send_custom_alert(a[ty-1],title,msg)

# default callbacks        
def _default_music_play():
    print("Played 1")
    send_notif('lkjdgkldfjgdfg')
def _default_music_pause():
    print("Paused 2")
def _default_music_forward():
    print("Forward 3")
def _default_music_back():
    print("Backward 4 ")
def _default_music_vup():
    print("volume up 5")
def _default_music_vdown():
    print("volume down 6 ")
def _default_music_focus_in():
    print("Music focus in 7")
def _default_music_focus_out():
    print("Music focus out 8")    


def set_music(): 
    band.setMusicCallback(_default_music_play,_default_music_pause,_default_music_forward,_default_music_back,_default_music_vup,_default_music_vdown,_default_music_focus_in,_default_music_focus_out)
    fi = input("Set music track artist to : ")
    fj = input("Set music track album to: ")
    fk = input("Set music track title to: ")
    fl = int(input("Set music volume: "))
    fm = int(input("Set music position: "))
    fn = int(input("Set music duration: "))
    band.setTrack(MUSICSTATE.PLAYED,fi,fj,fk,fl,fm,fn)
    while True:
        if band.waitForNotifications(0.5):
            continue
    input("enter any key")

if __name__ == "__main__":
    success = False
    while not success:
        try:
            if (AUTH_KEY):
                band = miband(MAC_ADDR, AUTH_KEY, debug=True)
                success = band.initialize()
            else:
                band = miband(MAC_ADDR, debug=True)
                success = True
            break
        except BTLEDisconnectError:
            print('Connection to the MIBand failed. Trying out again in 3 seconds')
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nExit.")
            exit()


set_music()
sadsadas