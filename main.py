#import section (this imports really important thiings. please dont remove it)

import os
import sys
import requests
import time

def pref(optionchoosen):
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    if optionchoosen=="path":
        with open(current_dir+"/pref.uwu", "r", encoding="utf-8") as file:
           lines = file.readlines()
        line_number = 1
        return lines[line_number - 1].strip()
        

# we love variables

pathtoprog = pref("path")
dumbinput = sys.argv[1]

#dumb shit functions section

def updatemode():
    while True:
        print("  ")
    return 0

# the User Input Section (UIS) (give here a trademark) (kill me)
def noargs():
      print("no arguments provided. Please use something called 'terminal' to use Unified Wor- blahblahblah")
      print("Press Enter to exit...")
      input()

      exit

if __name__ == "__main__":
    os.mkdir("~/.unifiedwu/temp")
    pref()
    print("""
    Unified Workspace Updater belongs to Nanoworks Group and was made by smieciarkosiarka
    Unified Workspace Updater is on license GPLv3
    
    Thank you!
     
     
    """)
    if len(sys.argv) < 2:
        noargs()
    
    if dumbinput == "start":
        updatemode()