#import section (this imports really important thiings. please dont remove it)


import os
import sys
import requests
import time

def pref(optionchoosen):
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    if optionchoosen=="path":
        print("get PATH from pref")
        with open(current_dir+"/pref.uwu", "r", encoding="utf-8") as file:
           lines = file.readlines()
        line_number = 1
        return lines[line_number - 1].strip()
    if optionchoosen=="server":
        print("get SERVER from pref")
        with open(current_dir+"/pref.uwu", "r", encoding="utf-8") as file:
           lines = file.readlines()
        line_number = 2
        print(lines[line_number - 1].strip())
        return lines[line_number - 1].strip()
    elif optionchoosen=="sleep":
        print("get SLEEP from pref")
        with open(current_dir+"/pref.uwu", "r", encoding="utf-8") as file:
           lines = file.readlines()
        line_number = 3
        return lines[line_number - 1].strip()
        


# we love variables

pathtoprog = pref("path")
dumbinput = sys.argv[1]

#dumb shit functions section

def updatemode():
    while 1==1:
        print("fun updatemode start")
        response = requests.get(pref("server") + "/tree.txt")
        print(str(response.status_code))
        print(response.status_code)
        print(len(str(response.text)))
        temptree = response.text

        path = os.path.expanduser("~/.unifiedwu/temp/tree.uwu")
        with open(path, "w", encoding="utf-8") as f:
           f.write(temptree)

        
        masssaver()
        time.sleep(int(pref("sleep")))

# a little help: to get current directory for the file, f"{os.path.expanduser(pref('path'))}/{curnam}"

def masssaver(): # this shit would update the users project.
    print("fun massaver start")
    line_count = 0
    with open(os.path.expanduser("~/.unifiedwu/temp/tree.uwu"), 'r', encoding="utf-8") as file:  # get the number of files in the project
        for line in file:
            line_count += 1
    print("Total lines:", line_count)
    # get the X line,read the name, get code and update (or create) the file
    cursec = 0
    with open(os.path.expanduser("~/.unifiedwu/temp/tree.uwu"), 'r', encoding="utf-8") as file:
        allines = file.readlines()
    while not cursec>line_count:
        try:
            curnam = allines[cursec]
        except IndexError:
            print("list out of range. BREAK")
            break
        print(f"requesting file {curnam}")
        curreq = requests.get(f"{pref('server')}/uwuupd/{curnam}")
        print(f"request get stats: len {len(curreq.text)} and code {curreq.status_code}")
        curcon = curreq.text

        if os.path.exists(os.path.expanduser(f"{pref('path')}/{curnam}")):
            print("tree.uwu file exists. no need for further actions")
        else:
            print("tree.uwu does not exist. creating the file...")
            open(os.path.expanduser(f"{pref('path')}/{curnam}"), "w").close()
        with open(f"{os.path.expanduser(pref('path'))}/{curnam}","w", encoding="utf-8") as f:
            f.write(curcon)
            print(f"wrote {len(curcon)} chars to {pref('path')+f'/{curnam}'}")
            cursec+=1
        

# the User Input Section (UIS) (give here a trademark) (kill me)
def noargs():
    print("no arguments provided. Please use something called 'terminal' to use Unified Wor- blahblahblah")
    input("Press Enter to exit...")
    exit()


if __name__ == "__main__":
    if os.path.exists(os.path.expanduser("~/.unifiedwu")):
        print("unifiedwu folder exists. no need for further actions")
    else:
        print("unifiedwu folder does not exist. creating directory...")
        os.mkdir(os.path.expanduser("~/.unifiedwu"))


    if os.path.exists(os.path.expanduser("~/.unifiedwu/temp")):
        print("unifiedwu/temp folder exists. no need for further actions")
    else:
        print("unifiedwu/temp folder does not exist. creating directory...")
        os.mkdir(os.path.expanduser("~/.unifiedwu/temp"))
    if os.path.exists(os.path.expanduser("~/.unifiedwu/temp/tree.uwu")):
        print("tree.uwu file exists. no need for further actions")
    else:
        print("tree.uwu does not exist. creating the file...")
        open(os.path.expanduser("~/.unifiedwu/temp/tree.uwu"), "w").close()
    

    
    print("""
    Unified Workspace Updater belongs to Nanoworks Group and was made by smieciarkosiarka
    Unified Workspace Updater is on license GPLv3
    
    Thank you!
     
     
    """)
    if len(sys.argv) < 2:
        noargs()
    
    if dumbinput == "start":
        updatemode()